import slack
from decouple import config


SLACK_TOKEN = config('SLACK_TOKEN')
client = slack.WebClient(token=SLACK_TOKEN)



client.chat_postMessage(channel='#a-better-yt', text='Hello world!')
