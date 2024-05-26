import praw
from langdetect import detect, LangDetectException
import csv

def get_reddit_comments(subreddit_name, client_id, client_secret, user_agent):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    subreddit = reddit.subreddit(subreddit_name)

    comments = []
    for submission in subreddit.hot(limit=15000):  
        submission.comments.replace_more(limit=0)  
        for comment in submission.comments.list():
            try:
                
                if detect(comment.body) == 'en':
                    comments.append(comment.body)
            except LangDetectException:
                
                continue

    return comments

def save_comments_to_csv(comments, filename):
    """Save the list of comments to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Comment'])  
        for comment in comments:
            writer.writerow([comment])  


client_id = 'client-id'
client_secret = 'client-secret'
user_agent = 'CommentExtractor by /u/yourusername'
subreddit_name = 'football'  

comments = get_reddit_comments(subreddit_name, client_id, client_secret, user_agent)
filename = 'reddit_english_comments4.csv'
save_comments_to_csv(comments, filename)
print(f"Saved {len(comments)} English comments to {filename}.")
