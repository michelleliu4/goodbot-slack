#from msilib.schema import Error
import datetime
import json
import os
from typing import Dict, List
from urllib import response
# Use the package we installed
from slack_bolt import App
from slack_sdk.errors import SlackApiError
import requests
import pprint
from blocks import block_dict
from slack_bolt.adapter.socket_mode import SocketModeHandler
import csv


# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])
channel_id = 'C04467M55B3'
p = pprint.PrettyPrinter()

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
            channel = channel_id, 
            text = text,
            token = os.environ.get("SLACK_BOT_TOKEN"),
            blocks = json.dumps(blocks) if blocks else None
        )
    except SlackApiError as e:
        print(e)


def schedule_messages(blocks: List[Dict[str, str]] = None):
    tomorrow = datetime.date.today() #+ datetime.timedelta(days=1)
    scheduled_time = datetime.time(hour=22, minute=45)
    schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')

    try:
        # Call the chat.scheduleMessage method using the WebClient
        result = app.client.chat_scheduleMessage(
            token = os.environ.get("SLACK_BOT_TOKEN"),
            text = f'SCHEDULED MESSAGE FOR {schedule_timestamp}',
            post_at= schedule_timestamp,
            channel = 'channel_id', 
            blocks = json.dumps(blocks) if blocks else None
        )
        
    except SlackApiError as e:
        print(e)



###LISTENERS### just playing around with them for now, not using any yet
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


@app.action("radio_buttons-action")
def handle_radio(ack, body, logger):
    ack()
    '''
    INPUT
    userID
    prompt which is text of block
    blockId to access response value
    response value
    [block_id, user_id, prompt, response]
    '''
    #logger.info(body)
    #p.pprint(body)
    userId = body['user']['id']
    blocks = body['message']['blocks']
    p.pprint(body)
    data_rows = []
    for b in blocks:
        if b['type'] != 'section':
            continue
        data_rows.append([b['block_id'], userId, b['text']['text']])
    for e in data_rows:
        b_id = e[0]
        selected = body['state']['values'][b_id]['radio_buttons-action']['selected_option']
        if selected:
            e.append(selected['value'])
    write_data(data_rows)

def write_data(data):
    with open('radio_actions.csv', 'w') as f:
        '''
        read whole csv, update data
        wipe csv and put in updated data
        '''
        old_data = list(csv.reader(open('radio_actions.csv')))
        block_ids = set()
        for r in old_data:
            block_ids.add(r[0])

        for r1 in data:
            if len(r1) != 4: # if response does not exist (user has not selected yet)
                continue
            if r1[0] in block_ids:
                # linear search for matching entry
                for r2 in old_data:
                    if r1[0] == r2[0] and r[1] == r2[1]: # matching block ids and user ids
                        r2[3] = r1[3]
                        break
            else:
                old_data.append(r1)

        p.pprint(old_data)
        writer = csv.writer(f)
        for row in old_data:
            writer.writerow(row)

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
    #post_message_to_slack(text='hello world', blocks=block_dict['survey_block'])
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    #app.start(port=int(os.environ.get("PORT", 3000)))
    #schedule_messages(block_dict['sample_block'])