import os
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from collections import Counter

# RAKE and PyTextRank imports
from rake_nltk import Rake
import pytextrank

COMMON_FRENCH_WORDS = {
    "euh", "alors", "ben", "bon", "bah", "voilà", "tu vois", "enfin", "quoi",
    "c'est-à-dire", "hein", "genre", "tu sais", "bah oui", "eh bien", "d'accord",
    "ah bon", "écoute", "tu comprends", "en fait", "jour", "nuit", "heure",
    "temps", "chose", "année", "moment", "question", "réponse", "vraiment", "vois",
    "lieu", "été", "faire", "bien", "non", "oui", "aller", "passer"
}

def load_text(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def extract_keywords(text, num_keywords=50):
    # Load French language model
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(text)
    
    # Tokenization and filtering
    lemmatized_words = [
        token.lemma_.lower() for token in doc 
        if token.is_alpha and token.text.lower() not in STOP_WORDS and token.lemma_.lower() not in COMMON_FRENCH_WORDS
    ]
    
    # Calculate word frequencies using Counter
    word_freq = Counter(lemmatized_words)
    
    # Get the top N keywords
    keywords = dict(word_freq.most_common(num_keywords))
    
    return keywords, lemmatized_words

def extract_key_phrases(lemmatized_words, num_phrases=30):
    # Join tokens back into a single string for phrase extraction
    text = " ".join(lemmatized_words)
    
    # Use CountVectorizer to extract bigrams/trigrams
    vectorizer = CountVectorizer(ngram_range=(2, 3)) 
    X = vectorizer.fit_transform([text])
    
    # Extract feature names (phrases) and their frequencies
    freqs = X.toarray().flatten()
    features = vectorizer.get_feature_names_out()
    
    # Create a dictionary of phrase: frequency
    phrase_freq = dict(zip(features, freqs))
    
    # Sort by frequency
    sorted_phrases = sorted(phrase_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Return top N phrases
    top_phrases = dict(sorted_phrases[:num_phrases])
    return top_phrases

def visualize_word_cloud(keywords):
    colors = LinearSegmentedColormap.from_list(
        "Colors", ["green", "beige", "darkgreen"], N=256
    )
    
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap=colors
    ).generate_from_frequencies(keywords)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Extracted Keywords")
    plt.show()

def visualize_bar_chart(data, title='Top Terms'):
    terms = list(data.keys())
    freqs = list(data.values())
    
    plt.figure(figsize=(10, 6))
    plt.barh(terms, freqs, color='darkgreen')
    plt.xlabel('Frequency')
    plt.ylabel('Terms')
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.show()

def extract_keywords_rake(text, num_keywords=15):
    
    rake = Rake(language='french', stopwords=STOP_WORDS) # Initialize RAKE
    rake.extract_keywords_from_text(text)
    
    
    ranked_phrases = rake.get_ranked_phrases()[:num_keywords] # Returns phrases with scores; extract top N
    # Convert to a dict for similarity measure (equal weighting)
    rake_keywords = {phrase: (num_keywords - i) for i, phrase in enumerate(ranked_phrases)}
    return rake_keywords

def extract_keywords_textrank(text, num_keywords=15):
    nlp = spacy.load("fr_core_news_sm")
    
    nlp.add_pipe("textrank") # Adding the "textrank" component directly to the pipeline
    doc = nlp(text)
    
    textrank_keywords = {}
    for phrase in doc._.phrases[:num_keywords]:
        textrank_keywords[phrase.text.lower()] = phrase.rank
    
    return textrank_keywords

def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union) if union else 0.0

if __name__ == "__main__":
    file_name = "interview_responses_new.txt"
    text = load_text(file_name)
    if text:
        # Our Method
        keyword_frequencies, lemmatized_words = extract_keywords(text, num_keywords=15)
        if keyword_frequencies:
            print("Top Keywords (Our Method):", list(keyword_frequencies.keys()))
        
            visualize_word_cloud(keyword_frequencies) # Word cloud
            visualize_bar_chart(keyword_frequencies, title='Top Keywords Extracted (Our Method)') # Bar chart

            key_phrases = extract_key_phrases(lemmatized_words, num_phrases=15)
            if key_phrases:
                print("Top Key Phrases (Our Method):", list(key_phrases.keys()))
                visualize_bar_chart(key_phrases, title='Top Key Phrases Extracted (Our Method)')
            
            # The following are the computations for computing keywords with other methods for evaluation purposes
            
            # RAKE's Method
            rake_keywords = extract_keywords_rake(text, num_keywords=15)
            print("Top Keywords (RAKE):", list(rake_keywords.keys()))
            
            # TextRank's Method
            textrank_keywords = extract_keywords_textrank(text, num_keywords=15)
            print("Top Keywords (TextRank):", list(textrank_keywords.keys()))
            
            our_method_set = set(keyword_frequencies.keys()) # Compare
            rake_set = set(rake_keywords.keys())
            textrank_set = set(textrank_keywords.keys())

            our_vs_rake = jaccard_similarity(our_method_set, rake_set)
            our_vs_textrank = jaccard_similarity(our_method_set, textrank_set)
            rake_vs_textrank = jaccard_similarity(rake_set, textrank_set)
            
            print(f"Jaccard Similarity (Our Method vs RAKE): {our_vs_rake:.4f}")
            print(f"Jaccard Similarity (Our Method vs TextRank): {our_vs_textrank:.4f}")
            print(f"Jaccard Similarity (RAKE vs TextRank): {rake_vs_textrank:.4f}")