from googleapiclient.discovery import build
from langdetect import detect, LangDetectException
import csv

def get_youtube_comments(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    try:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=100  # Adjust this to fetch more or fewer comments per request
        ).execute()

        while response:
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                try:
                    # Detect the language of the comment
                    if detect(comment) == 'en':
                        comments.append(comment)
                        print("Added an English comment.")  # Logging comment addition
                except LangDetectException:
                    print("Language detection failed and skipped a comment.")  # Error logging
                    continue

            # Checking if there is a next page
            if 'nextPageToken' in response:
                print("Fetching next page of comments...")
                response = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    textFormat='plainText',
                    pageToken=response['nextPageToken'],
                    maxResults=100
                ).execute()
            else:
                break
    except Exception as e:
        print("An error occurred: ", e)
    
    return comments

def save_comments_to_csv(comments, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Comment'])  # Writing header
        for comment in comments:
            writer.writerow([comment])  # Writing each comment

# Example usage
api_key = 'api-key'
video_id = '-5bcG6tZKx8'
print("Starting to fetch comments...")
comments = get_youtube_comments(video_id, api_key)
print(f"Collected {len(comments)} English comments.")
save_comments_to_csv(comments, 'youtube_english_comments8.csv')
print("Comments have been saved to 'youtube_english_comments8.csv'.")
