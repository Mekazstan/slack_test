# import os
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# from slack_sdk import WebClient

# app = Flask(__name__)

# load_dotenv()


# """_summary_
# Replace SLACK_BOT_TOKEN with the Slack Bot Token.
# 1. Get this from the Slack app's "OAuth & Permissions" page via link >> (https://api.slack.com/apps/)
# 2. Next, add scopes to the app to bot token. Scopes gives the app permission to perform actions, such as posting messages in a workspace. Scope type = chat:write
# 3. Click on Install to the workspace button.
# """
# slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
# slack_client = WebClient(token=slack_bot_token)


# """_summary_
# Replace with the ID of the channel where data is to be sent to.
# Find the channel ID of by right-clicking the channel name and selecting "Copy link." 
# The ID is the last part of the URL.
# """
# target_channel_id = os.getenv("CHANNEL_ID")

# @app.route("/slack/events", methods=["POST"])
# def handle_slack_events():
#     data = request.get_json()

#     if data["type"] == "block_actions":
#         actions = data["actions"]
#         if actions[0]["action_id"] == "confirm_forward_button":
#             # Extract the data from the form
#             values = data["state"]["values"]
#             full_name = values["full_name"]["full_name_input"]["value"]
#             passport_id = values["passport_id"]["passport_id_input"]["value"]
#             residential_address = values["residential_address"]["residential_address_input"]["value"]
#             email = values["email"]["email_input"]["value"]
#             phone_number = values["phone_number"]["phone_number_input"]["value"]
#             signing_date = values["signing_date"]["signing_date_input"]["value"]

#             # Format the data for the new channel
#             message = f"""
#             *Contract Data Forwarded:*
#             Full Name: {full_name}
#             Passport/ID: {passport_id}
#             Address: {residential_address}
#             Email: {email}
#             Phone: {phone_number}
#             Signing Date: {signing_date}
#             """

#             # Send the message to the "remote-workroom" channel
#             try:
#                 slack_client.chat_postMessage(channel=target_channel_id, text=message)
#                 return jsonify({"response_action": "clear"}) #Clears the message.
#             except Exception as e:
#                 print(f"Error sending message: {e}")
#                 return jsonify({"text": "Failed to forward data."}), 500

#     return jsonify({"challenge": data.get("challenge", "")})

# if __name__ == "__main__":
#     app.run(debug=True, port=3000)



import os
import logging
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from slack_sdk import WebClient

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

load_dotenv()

# Slack bot token and channel ID
slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
slack_client = WebClient(token=slack_bot_token)
target_channel_id = os.getenv("CHANNEL_ID")

@app.route("/slack/events", methods=["POST"])
def handle_slack_events():
    # Log the incoming request
    data = request.get_json()
    logger.debug(f"Received request: {data}")
    print(f"Received request: {data}")

    # Handle URL verification challenge
    if data.get("type") == "url_verification":
        logger.debug("Handling URL verification challenge")
        return jsonify({"challenge": data["challenge"]})

    # Handle button click (block_actions)
    if data.get("type") == "block_actions":
        logger.debug("Handling block_actions event")
        actions = data.get("actions", [])
        if actions and actions[0].get("action_id") == "confirm_forward_button":
            logger.debug("Button clicked: confirm_forward_button")

            # Extract data from the button's value (if needed)
            button_value = actions[0].get("value", "")
            logger.debug(f"Button value: {button_value}")

            # Send a message to the target channel
            try:
                message = f"Button clicked! Value: {button_value}"
                logger.debug(f"Sending message to channel {target_channel_id}: {message}")
                slack_client.chat_postMessage(channel=target_channel_id, text=message)

                # Delete the original message (optional)
                logger.debug("Deleting original message")
                slack_client.chat_delete(channel=data["container"]["channel_id"], ts=data["container"]["message_ts"])

                return jsonify({"text": "Data forwarded successfully."})
            except Exception as e:
                logger.error(f"Error sending message: {e}")
                logger.error(f"Payload received: {data}")  # Log the payload for debugging
                return jsonify({"text": "Failed to forward data."}), 500

    # Log unhandled event types
    logger.warning(f"Unhandled event type: {data.get('type')}")
    return jsonify({"text": "Unhandled event type."}), 200

if __name__ == "__main__":
    logger.info("Starting Flask app on port 3000")
    app.run(debug=True, port=3000)