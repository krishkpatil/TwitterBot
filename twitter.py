from sys import api_version
import tweepy, openai, random

api_key = 'YDed5euNKzfM8kuQSW2OlvH2L'
api_key_secret = 'UgN7lKSGhGUcn37dXjb6tNAiQgppjnNytQZ1XOChXxMqvIN9Gi'
access_key = "1222898182658510855-X4RLTxXJ8T3ShfXaph6XelDRfCrROw"
access_secret = "IBoidmnvBQC9cXCdzLx5JgqIQIN0yCBPOeWZHoI4X02MK"

openai_key = "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"

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
