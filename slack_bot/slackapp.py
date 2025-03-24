import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
import logging
import json  # import json

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
CHANNEL_ID = os.getenv("CHANNEL_ID")
FORWARD_CHANNEL_ID = os.getenv("FORWARD_CHANNEL_ID")

app = App(token=SLACK_BOT_TOKEN)
logging.basicConfig(level=logging.DEBUG)

# Slack event handlers
@app.event("message")
def handle_message_events(body, logger):
    logger.info("An event has been triggered!!")

@app.event("app_mention")
def handle_app_mention_events(body, logger, say):
    say("Hello :wave:")

def send_data_to_slack(webhook_data):  # Changed function name
    print("Now in slackapp")
    print("Type of webhook_data:", type(webhook_data))  # debug print
    print("webhook_data:", webhook_data)  # debug print

    try:
        webhook_data = json.loads(webhook_data)  # Parse string into list.
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return

    # Extract labels and add submit button
    labels = {}
    for block in webhook_data:
        if block["type"] == "input":
            block_id = block["block_id"]
            label = block["label"]["text"]  # Get the label
            labels[block_id] = label

    webhook_data.append(
        {
            "type": "actions",
            "block_id": "form_submit",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Submit",
                    },
                    "action_id": "form_submit_button",
                    "style": "primary",
                }
            ],
        }
    )

    # Store labels in app data (we'll need this later)
    app.view_labels = labels
    print("LABELS:", labels) # Debug print of labels.

    # Send the data as blocks to Slack
    try:
        client = WebClient(token=SLACK_BOT_TOKEN)
        client.chat_postMessage(
            channel=CHANNEL_ID,
            text="Please fill out the form below:",
            blocks=webhook_data,
        )
    except Exception as e:
        logging.error(f"Error sending message: {e}")
        
@app.action("form_submit_button")  # Changed action_id to match button
def handle_form_submit(ack, body, client, logger):
    ack()

    # Get form data
    form_data = {}
    for block in body["state"]["values"].values():
        for action_id, value in block.items():
            form_data[action_id] = value["value"]

    # Construct the message with all collected data
    message = "Form Submission 👍\n\n"
    for key, value in form_data.items():
        # Get the label for the field from app data
        block_id = key.replace("_input", "")
        # Get the label for the field from app.view_labels
        label = app.view_labels.get(block_id, key)
        message += f"*{label}:* {value}\n"

    # Extract Excess URL (assuming it's in the webhook data)
    excess_url = None
    for block in body["message"]["blocks"]:
        if block["type"] == "section" and block.get("block_id") == "contract_info_2":
            for field in block.get("fields",):
                if "*Excess URL:*" in field["text"]:
                    excess_url = field["text"].split("*Excess URL:* ")[1].strip()
                    break
        if excess_url:
            break

    if excess_url:
        message += f"\n*Excess URL:* {excess_url}\n"

    # Send the confirmation message to another channel
    target_channel_id = FORWARD_CHANNEL_ID
    try:
        client.chat_postMessage(channel=target_channel_id, text=message)
        logger.info(f"Message sent to channel {target_channel_id}")
    except Exception as e:
        logger.error(f"Error sending message to channel {target_channel_id}: {e}")

    # Send the confirmation message to the current channel
    try:
        client.chat_postMessage(
            channel=body["channel"]["id"], text="Form details sent."
        )
        logger.info(f"Confirmation sent to user in channel {body['channel']['id']}")
    except Exception as e:
        logger.error(f"Error sending confirmation to user: {e}")

def start_slack_app():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    logging.info("Starting Socket Mode Handler")
    handler.start()

if __name__ == "__main__":
    start_slack_app()