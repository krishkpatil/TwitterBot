from sys import api_version
import tweepy, openai, random

api_key = 'YOUR API KEY'
api_key_secret = 'YOUR API KEY'
access_key = "YOUR API KEY"
access_secret = "YOUR API KEY"

openai_key = "YOUR API KEY"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

openai.api_key = openai_key

prompts = [
    {
        "text": "tweet a funny fact"
    },
    {
        "text": "tweet something funny at elon musk"
    },
    {
        "text": "tweet something funny about crypto"
    },
    {
        "text": "funny pickup line"
    },
    {
        "text": "tweet something wholesome"
    },
    {
        "text": "tweet something about relationships"
    },
    {
        "text": "tweet something about stocks"
    },
    {
        "text": "tweet something about going to the gym"
    },
    {
        "text": "tweet something about soccer"
    }
]

chosen_prompt = random.choice(prompts)
text_openai = chosen_prompt["text"]

response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=text_openai,
    max_tokens=64
)
text = response.choices[0].text
print(text)
api.update_status(text)
