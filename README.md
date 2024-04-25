# Development of an Article Retrieval System

## Description
The repository contains an Article Retrieval System from dataset downloaded from the [kaggle.com](https://www.kaggle.com/datasets/meruvulikith/1300-towards-datascience-medium-articles-dataset/data). It contains collection of blog posts sourced from Medium.
The system is created in the main.ipynb notebook, while the app.py file contains an application that facilitates entering prompts and reading returned article fragments.

### Setup
After cloning the repository, install the required libraries in the virtual environment, you can do it with the command:
```
pip install -r requirements.txt
```
After this run file main.ipynb to create vector store. You can then use the app.py file to search for relevant fragments of articles.

### Operation
To run an app, write this command in your terminal:
```
streamlit run app.py
```