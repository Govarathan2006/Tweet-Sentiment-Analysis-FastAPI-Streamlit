#Tweet Sentiment Analysis Web App

This project is a Machine Learning-based Tweet Sentiment Analysis system that predicts whether a given text expresses Positive, Neutral, Negative, or Irrelevant sentiment.

The model is trained using a tweet dataset from Kaggle and deployed using a modern web architecture with FastAPI for the backend and Streamlit for the frontend.

Users can enter any text, and the system preprocesses the input, converts it into numerical features using TF-IDF, and predicts the sentiment in real time.

Project Workflow

Import required libraries
Load the tweet dataset
Clean missing values
Split the dataset into training and testing sets
Build a machine learning pipeline
Use TF-IDF Vectorizer to convert text data into numerical features
Train the model using Random Forest Classifier
Predict the test dataset
Evaluate model performance using accuracy metrics
Achieved 89% accuracy
Save the trained model using Joblib
Create REST API using FastAPI
Build the web interface using Streamlit

Technologies Used

Python
Pandas
NumPy
scikit-learn
FastAPI
Streamlit
Joblib

Model Details

Feature Extraction: TF-IDF
Algorithm: Random Forest Classifier
Accuracy: 89%
Task Type: Multi-class Text Classification
