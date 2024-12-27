# Movie Recommendation System

## Overview
Launched in 1997, online movie services have revolutionized how people access and enjoy films, with platforms offering thousands of movies at their fingertips. This Python-based project uses TMDb data to build a movie recommendation system that provides users with personalized movie suggestions based on similarity scores, presented through an interactive Streamlit web application.

## Objectives
1. Process TMDb data to create `.pkl` files for efficient data handling.
2. Recommend movies similar to the one selected by the user.
3. Fetch and display movie posters along with recommendations.
4. Enhance user experience using an intuitive web app.

## Workflow
1. **Data Preparation**:
   - The TMDb dataset is read from a CSV file in the Jupyter notebook.
   - Data preprocessing is performed, including:
     - Cleaning the data.
     - Calculating similarity scores using a content-based approach.
   - Two `.pkl` files are created:
     - `movies.pkl`: Contains processed movie data.
     - `similarity.pkl`: Contains the similarity matrix for recommendations.
2. **Frontend**:
   - The `main.py` script uses `Streamlit` to create an interactive web interface for the recommendation system.

## Features
- **Recommendation Engine**:
  - Suggests 12 similar movies for a selected input.
  - Leverages a similarity matrix to compute recommendations.
- **Poster Fetching**:
  - TMDb API fetches and displays movie posters.
- **Interactive Web App**:
  - Users can select movies and view recommendations seamlessly.

## Technologies Used
- **Python**: Main programming language.
- **Libraries**:
  - `pandas` for data processing.
  - `pickle` for saving and loading preprocessed data.
  - `streamlit` for frontend development.
  - `requests` for TMDb API integration.
- **Tools**:
  - Jupyter Notebook for preprocessing and `.pkl` file creation.
  - Streamlit for creating the web app.

## Setup and Usage
1. Clone this repository.
2. Install required libraries:
   ```bash
   pip install pandas streamlit requests
3. Prepare `.pkl` files:
   - Open the Jupyter notebook (`Movie Recommendation System.ipynb`).
   - Run the preprocessing steps to generate `movies.pkl` and `similarity.pkl`.
4. Update the `fetch_poster` function in `main.py` with your TMDb API key.
5. Run the Streamlit app:
   ```bash
   streamlit run main.py
