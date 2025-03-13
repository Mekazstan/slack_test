# Key Steps:

## Replace Placeholders:
- YOUR_SLACK_BOT_TOKEN: Get this from your Slack app's "OAuth & Permissions" page.
- YOUR_REMOTE_WORKROOM_CHANNEL_ID: Find the channel ID of "remote-workroom" by right-clicking the channel name and selecting "Copy link." The ID is the last part of the URL.

## Save and Run:
- Save the code as a Python file (e.g., app.py).
- Install the necessary libraries: pip install flask slack_sdk.

## Run the app: 
- python3 main.py

## Expose Your Server:
- Use ngrok to expose your local server to the internet.
- Run ngrok http 3000 (or the port you chose).
- Copy the ngrok forwarding URL (e.g., https://your-random-string.ngrok.io).


# Update Your Slack App Settings

**Go to Slack API:** Open api.slack.com/apps.
**Select Your App:** Choose the app you created for the Block Kit.

# Interactivity & Shortcuts:
- Go to "Interactivity & Shortcuts."
- Make sure "Interactivity" is enabled.
- Paste the ngrok forwarding URL into the "Request URL" field, adding /slack/events to the end (e.g., https://your-random-string.ngrok.io/slack/events).
- Click "Save Changes."

# Test the Workflow

**Open Slack:** Go to your "all-huddle-team" channel.
**Interact with the App:** Fill in the form fields.
**Click "Confirm&Forward":**
**Check "remote-workroom":** The data should appear in the "remote-workroom" channel.