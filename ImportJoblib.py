import joblib
import os

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Construct the relative path to the pkl file
pkl_path = os.path.join(current_dir, 'tfidf_vectorizer.pkl')

# Load the pkl file
tfidf_vectorizer = joblib.load(pkl_path)
