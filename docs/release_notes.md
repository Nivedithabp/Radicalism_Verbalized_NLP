# Release Notes

## Version 4.0.0 (Bug Fixes, Refactoring as .py files, and CLI)

- Fixed bug related to repeated words in keyword extractor. In general improved performance of keyword extraction with SpaCy by adding custom French common/stopwords.
  - Titled *Updated_Keyword_Extraction.ipynb*
- Improve output for Topic Modeling to return a .csv of the topics extracted.
- Refactored topic modeling code as a .py project and re-organized project structure.
  - Set up and tested running the topic modeling through the Command Line.
- Created .sh scripts for facilitating running the .py projects.
- Added a more robust docs/ section.
  - Index
  - Release Notes
  - Installation
  - Updated Usage
  - Methodologies on what's getting these results (what's going on under the hood)

## Version 3.0.0 (Docling & Keywords Strengths)

- Introduced support for Document Linguistic features (Docling).
- Added support for keyword strengths in the topic modeling module.
- Pushed notebook displaying our training experiments for BERT based Cognitive Bias Classification.
- Fixed bugs related to file paths.

## Version 2.0.0 (Cognitive Bias Classifier)

- Created Prompt-based Cognitive Bias classifier.
- Setup integration with Gradio.

## Version 1.6.0 (Topic Modeling + Neo4j)

- Added a Neo4j integration for Topic Modeling.
- Changing keyword extraction to French.
- Organizing README installation instructions.

## Version 1.5.0 (Topic Modeling)

- Basic functionality for keyword extraction

## Version 1.0.0 (Initial Release)

- Basic functionality for keyword extraction
