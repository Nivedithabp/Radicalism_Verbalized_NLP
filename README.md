# Radicalism_Verbalized_NLP

# Setup Instructions

#### 1. Clone the Repository

```
git clone https://github.com/Nivedithabp/Radicalism_Verbalized_NLP.git
```

#### 2. Install Dependencies
 - *NOTE*: python version **3.10** or greater is required.
```
pip install -r requirements.txt

```

---

#### 3. Running Task 1: *Keyword/Key Phrase Extraction*

 - The first thing you'll want to ensure is that you have made the text you want processed accesibile by the keyword extraction. There are two ways to do this:
     - 1. When prompted by the notebook, if you want manually enter your text, you can type ```text``` in the prompt window. You will then be prompted a second time to enter you text manually.
     - 2. If you want to read in a text file, type in ```file```, which will have it be read from the related folder it's been uploaded from.
         - A note on option #2: We will want to have an open dialouge about what will be easiest for the team regarding making their files readable. We can have a back-and-forth dialouge about this and adjust.
 - Once the data is read, the keyword/key-phrase extractors should be able to do the rest. After it's decided which one yields the best results, we can work on writing that to a save file.
---

#### 4. Task 2: *Topic Modeling*

- Firstly, before running the notebook to extract Topics from the text, sign up for Neo4j.
- Run the Jupyter notebook, **topic_modeling.ipynb**, after having entered the desired data to run Topic and extraction on.
     - Similar to the `file` option above in Task 1, this will look very similar. We will want to adjust this for what works best.
---
#### 5. Task 3: *Cognitive Bias Classification*


---