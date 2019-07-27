import requests
import os

def send_slack_notification(msg):
    try:
        slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')
        r = requests.post(slack_webhook_url, json={'text': msg})
    except requests.exceptions.RequestException as e:
        print(e)

