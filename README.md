# 🎬 Content-Based Movie Recommender System

A Content-Based Movie Recommendation System built using the TMDB 5000 Movie Dataset. The system recommends movies similar to a selected movie by analyzing textual features such as genres, keywords, cast, crew, and overview.

The recommendation engine uses Natural Language Processing (NLP) techniques, Bag of Words, and Cosine Similarity to identify similar movies.

---

## Features

- Recommend top 5 similar movies
- Interactive Streamlit web application
- Content-based recommendation
- NLP preprocessing
- Fast similarity lookup using precomputed cosine similarity matrix

---

## Dataset

TMDB 5000 Movie Dataset

Files used:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Pickle
- Streamlit

---

## Project Workflow

```
TMDB Dataset
      │
      ▼
Merge Movies + Credits
      │
      ▼
Feature Selection
      │
      ▼
Missing Value Handling
      │
      ▼
Extract

• Genres
• Keywords
• Cast
• Director
• Overview

      │
      ▼
Create Combined Tags
      │
      ▼
Text Preprocessing

• Lowercase
• Remove Spaces
• Stemming

      │
      ▼
CountVectorizer
(Bag of Words)

      │
      ▼
Cosine Similarity Matrix

      │
      ▼
Recommend Top 5 Movies
```

---

## Machine Learning Concepts Used

### Feature Engineering

The following movie attributes are combined into a single textual feature:

- Overview
- Genres
- Keywords
- Top 3 Cast Members
- Director

---

### Text Preprocessing

- Missing value handling
- JSON parsing
- Tokenization
- Stemming using Porter Stemmer

---

### Vectorization

Movies are converted into numerical vectors using:

**CountVectorizer**

- Maximum Features = 5000
- English Stop Words Removed

---

### Similarity Measure

Cosine Similarity is computed between every pair of movies.

Movies having the highest cosine similarity score are recommended.

---

## Project Structure

```
Movie-Recommender-System/
│
├── app.py
├── Content_Based_Recommender.ipynb
├── generate_pickle.py
├── requirements.txt
├── README.md
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── screenshots/
    └── homepage.png
```

Run the notebook (or generate_pickle.py) once to generate:

movies.pkl
similarity.pkl

These files are not included because of GitHub size limits.

---

## Installation

Clone the repository

```bash
git clone https://github.com/bhargavanarasimhaai24/Content-Based-Movie-Recommendation-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Example

Input:

Spider-Man 3

Output:

- Spider-Man 2
- Spider-Man
- The Amazing Spider-Man 2
- The Amazing Spider-Man
- Arachnophobia

---

## Future Improvements

- Display movie posters using TMDB API
- Show movie ratings
- Show genres and release year
- Add movie overview
- Search bar with autocomplete
- Hybrid recommendation system
- Collaborative filtering
- Deep Learning based embeddings

---

## Author

Developed as an NLP and Machine Learning project using the TMDB Movie Dataset.
