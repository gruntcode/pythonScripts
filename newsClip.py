import requests
import time
from gtts import gTTS

# Define your NewsAPI key here
api_key = 'your api key'

# Define the endpoint URL
url = 'https://newsapi.org/v2/top-headlines'

# Define the news categories 'technology','health','business', 'science',
categories = ['general']

news_summaries = []

# Loop through each category
for category in categories:
    # Define the parameters for the request
    parameters = {
        'q': category,  # Query
        'pageSize': 2,  # Number of articles to return
        'apiKey': api_key  # Your API key
    }

    # Send the request
    response = requests.get(url, params=parameters)

    # Make sure the request was successful
    response.raise_for_status()

    # Convert the response to JSON
    data = response.json()

    # Loop through the news stories
    for article in data['articles']:
        # Extract the title, description and content
        title = article['title']
        description = article['description']
        content = article['content']
        # Create a summary of the news story
        news_summary = f'{title}. {description}. {content}'
        # Add the news summary to the list
        news_summaries.append(news_summary)

# Save the news summaries to a file
with open('news_summaries.txt', 'w') as f:
    f.write('\n\n'.join(news_summaries) + '\n\n')

time.sleep(3)

# Open the news summaries file
with open('news_summaries.txt', 'r') as f:
    # Read the news summaries
    news_summaries = f.readlines()

# Create the prompt for the voiceover
prompt = 'Here are the trending news stories for this week in business, technology, and science. Don’t forget to like and subscribe and of course hit the notification bell so you get your weekly notification '
for i, news_summary in enumerate(news_summaries, start=1):
    prompt += f'In {news_summary}. '

# Add a conclusion prompt
prompt += 'Well thats all for this weeks news roundup. Thank you for watching and listening! see you on the next one'

# Create a gTTS object
tts = gTTS(prompt, lang='en')

# Save the voiceover to a file
tts.save('voice.mp3')

print("Process completed successfully. The voiceover file has been saved as 'voice.mp3'.")

# End of script
