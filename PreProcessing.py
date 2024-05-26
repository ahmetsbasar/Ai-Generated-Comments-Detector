import pandas as pd
import re
import numpy as np

# Load the datasets
youtube_df = pd.read_csv("Final_Youtube_Comments.csv")
reddit_df = pd.read_csv("Final_Reddit_Comments.csv")
ai_generated_df = pd.read_csv("Final_Generated_Comments.csv")

# Print column names to verify
print("YouTube DataFrame columns:", youtube_df.columns)
print("Reddit DataFrame columns:", reddit_df.columns)
print("AI Generated DataFrame columns:", ai_generated_df.columns)

# Step 2: Clean the Text Data
def clean_text(text):
    if pd.isnull(text):  # Check for NaN values
        return ""  # Return an empty string for NaN values
    text = str(text)  # Convert to string to handle NaN values
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    text = remove_emojis(text)  # Remove emojis
    return text

def remove_emojis(text):
    emoji_pattern = re.compile(
        "[" 
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)


# Apply the clean_text function to the comments in each DataFrame
youtube_df['Comment'] = youtube_df['Comment'].apply(clean_text)
reddit_df['Comment'] = reddit_df['Comment'].apply(clean_text)
ai_generated_df['Comment'] = ai_generated_df['Generated Comments'].apply(clean_text)

# Remove rows with empty 'Comment' column
youtube_df = youtube_df[youtube_df['Comment'] != '']
reddit_df = reddit_df[reddit_df['Comment'] != '']
ai_generated_df = ai_generated_df[ai_generated_df['Comment'] != '']

# Step 3: Label the Data
youtube_df['label'] = 0
reddit_df['label'] = 0
ai_generated_df['label'] = 1

# Step 4: Combine the Datasets
youtube_df['source'] = 'youtube'
reddit_df['source'] = 'reddit'
ai_generated_df['source'] = 'ai_generated'

# Concatenate the DataFrames
combined_df = pd.concat([youtube_df[['Comment', 'label', 'source']], 
                         reddit_df[['Comment', 'label', 'source']], 
                         ai_generated_df[['Comment', 'label', 'source']]], 
                        ignore_index=True)

# Shuffle the DataFrame
combined_df = combined_df.sample(frac=1).reset_index(drop=True)

# Save the combined and preprocessed dataset to a new CSV file
combined_df.to_csv("final_preprocessed_combined_comments3.csv", index=False)

print("Data preprocessing completed successfully. Combined data saved to 'preprocessed_combined_comments.csv'.")
