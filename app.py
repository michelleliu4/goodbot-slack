#from msilib.schema import Error
import datetime
import json
import os
import slack
from typing import Dict, List
# Use the package we installed
from slack_bolt import App
from slack_sdk.errors import SlackApiError
import requests
from blocks import block_dict
from slack_bolt.adapter.socket_mode import SocketModeHandler


from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Initializes your app with your bot token and signing secret
print(os.environ.get("SLACK_BOT_TOKEN"))
print(os.environ.get("SLACK_SIGNING_SECRET"))
print(os.environ.get("SLACK_APP_TOKEN"))

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

def post_message_to_slack(text: str, blocks: List[Dict[str, str]] = None):
    print(os.environ.get("SLACK_BOT_TOKEN"))
    try:
        app.client.chat_postMessage(
            token = os.environ.get("SLACK_BOT_TOKEN"),
            text = '',
            channel = 'C043JK0TCEA', 
            blocks = json.dumps(blocks) if blocks else None
        )
    except:
        print('error')



hours = 23
minutes = 52
print(minutes)

def schedule_messages(blocks: List[Dict[str, str]] = None):
    tomorrow = datetime.date.today() #+ datetime.timedelta(days=1)
    scheduled_time = datetime.time(hour=hours, minute=minutes)
    schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')

    try:
        # Call the chat.scheduleMessage method using the WebClient
        result = app.client.chat_scheduleMessage(
            token = os.environ.get("SLACK_BOT_TOKEN"),
            text = f'SCHEDULED MESSAGE FOR {schedule_timestamp}',
            post_at= schedule_timestamp,
            channel = 'C043JK0TCEA', 
            blocks = json.dumps(blocks) if blocks else None
        )
        
    except SlackApiError as e:
        print(e)



#dictionary of resources to send back
helpful_resources = {}




BOT_ID = 'B043P5P2PEZ'
@app.event("message")
def message_response(payload, say):
    print(payload)
    channel_id = payload['channel']
    text  = payload['text']
    user_id = payload['user']
    print(text)

    if user_id != BOT_ID:
        # here is ideally the spot to run the sementiment analysis function
        if text == "hi":
            say("Hello")
        else:
            say("Hey")


        


##LISTENERS### just playing around with them for now, not using any yet
@app.shortcut("open_modal")
def open_modal(ack, shortcut, client, logger):

    # Acknowledge shortcut request
    ack()

    try:
        # Call the views.open method using the WebClient passed to listeners
        result = client.views_open(
            trigger_id=shortcut["trigger_id"],
            view={
                "type": "modal",
                "title": {"type": "plain_text", "text": "My App"},
                "close": {"type": "plain_text", "text": "Close"},
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "About the simplest modal you could conceive of :smile:\n\nMaybe <https://api.slack.com/reference/block-kit/interactive-components|*make the modal interactive*> or <https://api.slack.com/surfaces/modals/using#modifying|*learn more advanced modal use cases*>.",
                        },
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": "Psssst this modal was designed using <https://api.slack.com/tools/block-kit-builder|*Block Kit Builder*>",
                            }
                        ],
                    },
                ],
            },
        )
        logger.info(result)

    except:
        logger.error("Error creating conversation: {}")

@app.event("app_mention")
def event_test(say):
    say("Hi there!")

@app.message("knock knock")
def ask_who(message, say):
    print('askwho')
    say("_Who's there?_")

@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    print('update home tab!')
    try:
        # views.publish is the method that your app uses to push a view to the Home tab
        client.views_publish(
        # the user that opened your app's app home
            user_id=event["user"],
            # the view object that appears in the app home
            view={
                "type": "home",
                "callback_id": "home_view",

                # body of the view
                "blocks": [
                {
                    "type": "section",
                    "text": {
                    "type": "mrkdwn",
                    "text": "*Welcome to your _App's Home_* :tada:"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                    "type": "mrkdwn",
                    "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                    {
                        "type": "button",
                        "text": {
                        "type": "plain_text",
                        "text": "Click me!"
                        }
                    }
                    ]
                }
                ]
            }
        )
    
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")

@app.command("/echo")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{command['text']}")






# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    #app.start(port=int(os.environ.get("PORT", 3000)))
    schedule_messages(block_dict['sample_block'])

    
    
    
    