# Methodologies behind tooling

## Keyword Extraction:

*The following has been taken from Analytics Vidhya  : https://www.analyticsvidhya.com/blog/2022/03/keyword-extraction-methods-from-documents-in-nlp/*

#### RAKE

[**RAKE**](https://www.analyticsvidhya.com/blog/2021/10/rapid-keyword-extraction-rake-algorithm-in-natural-language-processing/) (Rapid Automatic Keyword Extraction) is a well-known [**keyword extraction**](https://www.analyticsvidhya.com/blog/2022/01/four-of-the-easiest-and-most-effective-methods-of-keyword-extraction-from-a-single-text-using-python/) method that finds the most relevant words or phrases in a text using a set of stopwords and phrase delimiters. Rake nltk is an expanded version of RAKE that [**NLTK**](https://www.analyticsvidhya.com/blog/2021/07/nltk-a-beginners-hands-on-guide-to-natural-language-processing/) supports. The steps for Rapid Automatic Keyword Extraction are as follows:

* Split the input text content by dotes
* Create a matrix of word co-occurrences
* Word scoring – That score can be calculated as the degree of a word in the matrix, as the word frequency, or as the degree of the word divided by its frequency
* keyphrases can also be created by combining the keywords
* A keyword or keyphrase is chosen if and only if its score belongs to the top T scores, where T is the number of keywords you want to extract

#### Textrank

[**Textrank**](https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/), a Python tool for keyword extraction and [**text summarization**](https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/), analyzes word relationships by examining their sequential occurrences. The algorithm employs the PageRank algorithm to rank the most significant terms in the text. This algorithm to extract keywords from text seamlessly integrates with the Spacy pipeline and executes the following key steps for keyword extraction:

* **Step 1:** Textrank constructs a word network (word graph) to identify relevant terms based on word co-occurrence. Words frequently found together in the text are linked, with stronger connections for higher frequency pairs.
* **Step 2:** The [**Pagerank algorithm**](https://www.analyticsvidhya.com/blog/2015/04/pagerank-explained-simple/) assesses word relevance within the network. The top third of terms are retained as significant. When relevant terms appear consecutively in the text, they are grouped in a keywords table.

Textrank, implemented in Python, offers swift and precise phrase extraction and extractive summarization, making it a valuable addition to spaCy workflows. This graph-based method is language-agnostic and does not rely on domain-specific knowledge. We’ll use PyTextRank, a Python version of TextRank integrated as a spaCy pipeline plugin for keyword extraction. To delve deeper into Textrank, refer to the base paper linked here.

#### KeyBert (Method used in Topic Modeling section more)

KeyBERT is a straightforward and user-friendly keyword extraction technique that leverages [**BERT embeddings**](https://www.analyticsvidhya.com/blog/2019/09/demystifying-bert-groundbreaking-nlp-framework/) to identify the most similar keywords and keyphrases within a given document. This algorithm to extract keywords from text relies on BERT embeddings and employs basic cosine similarity to pinpoint sub-documents within the text that closely resemble the document as a whole.

[**BERT**](https://www.analyticsvidhya.com/blog/2019/09/demystifying-bert-groundbreaking-nlp-framework/) is utilized to extract document embeddings to create a document-level representation. Subsequently, word embeddings for [**N-gram words**](https://www.analyticsvidhya.com/blog/2021/09/what-are-n-grams-and-how-to-implement-them-in-python/)/phrases are extracted. Finally, [**cosine similarity**](https://www.analyticsvidhya.com/blog/2024/06/cosine-similarity-in-python/#:~:text=This%20article%20will%20discuss%20cosine,data%20mining%2C%20and%20information%20retrieval.) is applied to identify words/phrases that closely resemble the document, allowing for the identification of terms that best encapsulate the entire document.

KeyBert utilizes huggingface transformer-based pre-trained models to generate embeddings, with the default choice being the all-MiniLM-L6-v2 model.

---

## Topic Modeling:

*From the BERTopic documentation: https://maartengr.github.io/BERTopic/index.html*

#### BERTopic

BERTopic is a topic modeling technique that leverages 🤗 transformers and c-TF-IDF to create dense clusters allowing for easily interpretable topics whilst keeping important words in the topic descriptions.

Furthermore, an excerpt on BERTopic's methodology from the [BERTopic ](https://arxiv.org/pdf/2203.05794)paper:

- "BERTopic, a topic model that extends the cluster embedding approach by leveraging state-of-the-art language models and applying a class-based TF-IDF procedure for generating topic representations. By separating the process of clustering documents and generating topic representations significant flexibility is introduced in the
  model allowing for ease of usability

In short, it combines state of the art Lanugage Modeling with TF-IDF clustering to get the topics most important to a document.

##### Keyword -> Strength Metric

*Calculated via a combination of language model embeddings and TF-IDF Variants*

The strength of a keyword **k** for a topic **𝑇** is typically calculated as:

- **TF-IDF Variants**: How unique and frequent
  **𝑘** is in documents within **𝑇**, adjusted by how commonly **𝑘** appears across all topics.
- **Embedding Similarity:** The cosine similarity between the embedding of **𝑘** and the centroid (average embedding) of the topic’s documents.
- **Class-Based TF-IDF (c-TF-IDF)**: BERTopic uses c-TF-IDF, which considers all documents in a topic as a "class" and assigns higher scores to words that distinguish the class.

#### Citation:

```
@article{grootendorst2022bertopic,
  title={BERTopic: Neural topic modeling with a class-based TF-IDF procedure},
  author={Grootendorst, Maarten},
  journal={arXiv preprint arXiv:2203.05794},
  year={2022}
}
```
