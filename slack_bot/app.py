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

# Define the form blocks
form_blocks = [
    {
        "type": "section",
        "block_id": "contract_info_1",
        "text": {
            "type": "mrkdwn",
            "text": "*Passport Name:* UY9990062\n*Contract Name:* HUSSAIN ISRAR HUSSAIN\n--\n*Contract Oncounter:* 6276\n*Contract:* 6276-MRA\n--\n*Excess sum Oncounter:* 3947.6\n*Sum from Invoice:* 3947.6\n--\n*Start Date Oncounter:* 02/02/2025 17:14:00\n*Start Date Contract:* 02-02-2025 17:14\n--\n*End Date Oncounter:* 27/02/2025 17:14:00\n*End Date Contract:* Not specified"
        }
    },
    {
        "type": "section",
        "block_id": "contract_info_2",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Excess URL:* https://oncounter.cardooworld.com/excess/829aa2bb-0919-4022-8c35-2b30b225a6d0"
            },
            {
                "type": "mrkdwn",
                "text": "*Phone number from Contract:* +123456789"
            },
            {
                "type": "mrkdwn",
                "text": "*Phone number from Invoice:* +123456789"
            },
            {
                "type": "mrkdwn",
                "text": "*E-mail from Contract:* ali@ya.ru"
            },
            {
                "type": "mrkdwn",
                "text": "*Email from Invoice:* ali@ya.ru"
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
        "block_id": "country",
        "label": {
            "type": "plain_text",
            "text": "Country"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "Country (Based on Passport ID)",
            "initial_value": "UAE"
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
        }
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
        }
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
        }
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
        }
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
        }
    },
    {
        "type": "input",
        "block_id": "car_number",
        "label": {
            "type": "plain_text",
            "text": "Car number"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "car_number_input",
            "initial_value": "1234556"
        }
    },
    {
        "type": "input",
        "block_id": "comment_id_number",
        "label": {
            "type": "plain_text",
            "text": "Comment"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "comment_id_number_input",
            "initial_value": "Type your comment here."
        }
    },
    {
        "type": "input",
        "block_id": "driver_license_number",
        "label": {
            "type": "plain_text",
            "text": "Driver License number"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "driver_license_number_input",
            "initial_value": "111-111 AB"
        }
    },
    {
        "type": "input",
        "block_id": "vehicle_model",
        "label": {
            "type": "plain_text",
            "text": "Vehicle model"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "vehicle_model_input",
            "initial_value": "BMW 5"
        }
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

# Slack event handlers
@app.event("message")
def handle_message_events(body, logger):
    logger.info("An event has been triggered!!")

@app.event("app_mention")
def handle_app_mention_events(body, logger, say):
    say("Hello :wave:")

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
def handle_confirm_forward(ack, body, client, logger):
    ack()

    # Extract input values
    values = body["state"]["values"]
    country = values["country"]["Country (Based on Passport ID)"]["value"]
    full_name = values["full_name"]["full_name_input"]["value"]
    passport_id = values["passport_id"]["passport_id_input"]["value"]
    residential_address = values["residential_address"]["residential_address_input"]["value"]
    email = values["email"]["email_input"]["value"]
    phone_number = values["phone_number"]["phone_number_input"]["value"]
    car_number = values["car_number"]["car_number_input"]["value"]
    comment = values["comment_id_number"]["comment_id_number_input"]["value"]
    driver_license_number = values["driver_license_number"]["driver_license_number_input"]["value"]
    vehicle_model = values["vehicle_model"]["vehicle_model_input"]["value"]

    # Extract the Excess URL from the static fields
    excess_url = None
    for block in form_blocks:
        if block.get("block_id") == "contract_info_2":
            for field in block["fields"]:
                if "*Excess URL:*" in field["text"]:
                    excess_url = field["text"].split("*Excess URL:* ")[1].strip()
                    break
            if excess_url:
                break

    # Construct the message with all collected data
    message = f"New User Details 👍\n\n"
    message += f"*Country:* {country}\n"
    message += f"*Full Name:* {full_name}\n"
    message += f"*Passport/ID:* {passport_id}\n"
    message += f"*Residential Address:* {residential_address}\n"
    message += f"*Email:* {email}\n"
    message += f"*Phone Number:* {phone_number}\n"
    message += f"*Car Number:* {car_number}\n"
    message += f"*Comment:* {comment}\n"
    message += f"*Driver License Number:* {driver_license_number}\n"
    message += f"*Vehicle Model:* {vehicle_model}\n"
    message += f"*Excess URL:* {excess_url}\n"

     # Send the confirmation message to another channel
    target_channel_id = CHANNEL_ID
    try:
        client.chat_postMessage(channel=target_channel_id, text=message)
        logger.info(f"Message sent to channel {target_channel_id}")
    except Exception as e:
        logger.error(f"Error sending message to channel {target_channel_id}: {e}")

    # Send the confirmation message to the current channel
    try:
        client.chat_postMessage(channel=body["channel"]["id"], text=f"{full_name}'s details sent.")
        logger.info(f"Confirmation sent to user in channel {body['channel']['id']}")
    except Exception as e:
        logger.error(f"Error sending confirmation to user: {e}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    logging.info("Starting Socket Mode Handler")
    handler.start()