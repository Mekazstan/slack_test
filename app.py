import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

app = App(token=SLACK_BOT_TOKEN)

logging.basicConfig(level=logging.DEBUG)

form_blocks = [
    {
        "type": "section",
        "block_id": "contract_info",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Passport Name:* UY9990062"
            },
            {
                "type": "mrkdwn",
                "text": "*Contract Name:* HUSSAIN ISRAR HUSSAIN"
            },
            {
                "type": "mrkdwn",
                "text": "*Contract Oncounter:* 6276"
            },
            {
                "type": "mrkdwn",
                "text": "*Contract:* 6276-MRA"
            },
            {
                "type": "mrkdwn",
                "text": "*Excess sum Oncounter:* 3947.6"
            },
            {
                "type": "mrkdwn",
                "text": "*Sum from Invoice:* 3947.6"
            },
            {
                "type": "mrkdwn",
                "text": "*Start Date Oncounter:* 02/02/2025 17:14:00"
            },
            {
                "type": "mrkdwn",
                "text": "*Start Date Contract:* 02-02-2025 17:14"
            },
            {
                "type": "mrkdwn",
                "text": "*End Date Oncounter:* 27/02/2025 17:14:00"
            },
            {
                "type": "mrkdwn",
                "text": "*End Date Contract:* Not specified"
            }
        ]
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "block_id": "consent_info",
        "text": {
            "type": "mrkdwn",
            "text": "*CONSENT*"
        }
    },
    {
        "type": "input",
        "block_id": "full_name",
        "label": {
            "type": "plain_text",
            "text": "Full name"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "full_name_input",
            "initial_value": "HUSSAIN ISRAR HUSSAIN"
        },
        "dispatch_action": False
    },
    {
        "type": "input",
        "block_id": "passport_id",
        "label": {
            "type": "plain_text",
            "text": "Passport / ID number"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "passport_id_input",
            "initial_value": "UY9990062"
        },
        "dispatch_action": False
    },
    {
        "type": "input",
        "block_id": "residential_address",
        "label": {
            "type": "plain_text",
            "text": "Residential address"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "residential_address_input",
            "initial_value": "403, C-6 MEYDAN, POLO RESIDENCES, DUBAI"
        },
        "dispatch_action": False
    },
    {
        "type": "input",
        "block_id": "email",
        "label": {
            "type": "plain_text",
            "text": "E-mail"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "email_input",
            "initial_value": "turihussain890@gmail.com"
        },
        "dispatch_action": False
    },
    {
        "type": "input",
        "block_id": "phone_number",
        "label": {
            "type": "plain_text",
            "text": "Phone number"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "phone_number_input",
            "initial_value": "971543337558"
        },
        "dispatch_action": False
    },
    {
        "type": "input",
        "block_id": "signing_date",
        "label": {
            "type": "plain_text",
            "text": "Date of signing"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "signing_date_input",
            "initial_value": "02-02-2025 00:00"
        },
        "dispatch_action": False
    },
    {
        "type": "actions",
        "block_id": "confirm_forward",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Confirm&Forward"
                },
                "action_id": "confirm_forward_button",
                "style": "primary"
            }
        ]
    }
]

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

@app.command("/test_form")
def handle_test_form(ack, body, client, logger):
    ack()
    try:
        client.chat_postMessage(
            channel=body["channel_id"],
            text="Please fill out the form below:",
            blocks=form_blocks,
        )
    except Exception as e:
        logger.error(f"Error sending message: {e}")

@app.action("confirm_forward_button")
def handle_confirm_forward(ack, body, client, logger, say):
    ack()

    # Extract input values
    values = body["state"]["values"]
    full_name = values["full_name"]["full_name_input"]["value"]
    passport_id = values["passport_id"]["passport_id_input"]["value"]
    residential_address = values["residential_address"]["residential_address_input"]["value"]
    email = values["email"]["email_input"]["value"]
    phone_number = values["phone_number"]["phone_number_input"]["value"]
    signing_date = values["signing_date"]["signing_date_input"]["value"]

    # Construct the message with input data
    message = f"New User Details 👍\n\n"
    message += f"*Full Name:* {full_name}\n"
    message += f"*Passport/ID:* {passport_id}\n"
    message += f"*Address:* {residential_address}\n"
    message += f"*Email:* {email}\n"
    message += f"*Phone:* {phone_number}\n"
    message += f"*Signing Date:* {signing_date}"

    # Send the confirmation message to another channel. Replace 'YOUR_TARGET_CHANNEL_ID'
    target_channel_id = CHANNEL_ID
    client.chat_postMessage(channel=target_channel_id, text=message)

    # Send the confirmation message to the current channel.
    client.chat_postMessage(channel=body["channel"]["id"], text=f"{full_name} details sent.")

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    logging.info("Starting Socket Mode Handler")
    handler.start()