import pandas as pd
import nltk
from textblob import TextBlob
from tqdm import tqdm

# Load the dataset
generated_df = pd.read_csv("final_featured_engineered_combined_comments3.csv")  # Change file name here

# Function for POS tagging
def pos_tagging(text):
    if isinstance(text, str):
        tokens = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(tokens)
        return pos_tags
    else:
        return []

# Function for sentiment analysis
def sentiment_analysis(text):
    if isinstance(text, str):
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return sentiment.polarity, sentiment.subjectivity
    else:
        return None, None

# Apply functions with progress bars
tqdm.pandas(desc="POS Tagging")
generated_df['pos_tags'] = generated_df['Comment'].progress_apply(pos_tagging)  # Changed column name here

tqdm.pandas(desc="Sentiment Analysis")
generated_df['sentiment_polarity'], generated_df['sentiment_subjectivity'] = zip(*generated_df['Comment'].progress_apply(sentiment_analysis))  # Changed column name here

# Save the updated dataset
generated_df.to_csv("final_featured_combined_comments_with_sentiment.csv", index=False)  # Change file name here

print("POS tagging and sentiment analysis completed successfully.")
