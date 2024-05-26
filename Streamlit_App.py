import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load the TF-IDF vectorizer and logistic regression model
tfidf_vectorizer = joblib.load('/Users/ahmetsbasar/Desktop/DetectingAIGeneratedComments/tfidf_vectorizer.pkl')
logistic_regression_model = joblib.load('/Users/ahmetsbasar/Desktop/DetectingAIGeneratedComments/logistic_regression_model.pkl')

def preprocess_comment(comment):
    # Preprocess the input comment
    comment_tfidf = tfidf_vectorizer.transform([comment])
    return comment_tfidf

def predict_comment_authenticity(comment):
    # Preprocess the input comment
    comment_tfidf = preprocess_comment(comment)
    
    # Make prediction
    prediction = logistic_regression_model.predict(comment_tfidf)
    return prediction

def main():
    st.title("AI Generated Comment Detector")
    st.write("Enter a comment to check its authenticity:")

    comment = st.text_input("Enter comment here:")

    if st.button("Check Authenticity"):
        if comment.strip() == "":
            st.error("Please enter a comment.")
        else:
            prediction = predict_comment_authenticity(comment)
            if prediction == 1:
                st.success("The comment is likely to be AI-generated.")
            else:
                st.success("The comment is likely to be genuine.")

if __name__ == "__main__":
    main()
