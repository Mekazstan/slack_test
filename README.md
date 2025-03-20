# How to Run the Slack Bot Code

This guide will walk you through the steps to set up and run the Slack bot code provided in the `app.py` file. I broke it down into simple, easy-to-follow steps.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setting Up Your Slack App](#setting-up-your-slack-app)
3. [Installing Required Tools](#installing-required-tools)
4. [Setting Up the Environment](#setting-up-the-environment)
5. [Running the Bot](#running-the-bot)
6. [Testing the Bot](#testing-the-bot)

---

## Prerequisites

Before you start, make sure you have the following:

1. **A Slack Workspace**: You need to have access to a Slack workspace where you can create and install apps.
2. **Basic Computer Skills**: You should know how to open a terminal or command prompt and run basic commands.
3. **Python Installed**: Ensure that Python is installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

---

## Setting Up Your Slack App

1. **Create a New Slack App**:
   - Go to the [Slack API](https://api.slack.com/apps) website.
   - Click on **"Create New App"**.
   - Choose **"From scratch"**.
   - Give your app a name (e.g., `Forward Service`) and select the workspace where you want to install it.
   - Click **"Create App"**.

2. **Add Bot Token Scopes**:
   - In the left sidebar, click on **"OAuth & Permissions"**.
   - Scroll down to **"Scopes"** and under **"Bot Token Scopes"**, add the following permissions:
     - `chat:write`
     - `commands`
     - `channels:read`
     - `channels:write`
     - `app_mentions:read`
     - `channels:history`
     - `channels:join`
     - `chat:write.public`
     - `groups:history`
     - `im:history`
     - `mpim:history`

   - Scroll up and click **"Install to Workspace"**.
   - After installation, you'll see a **"Bot User OAuth Token"**. Copy this token; you'll need it later.

3. **Enable Socket Mode**:
   - In the left sidebar, click on **"Socket Mode"**.
   - Toggle the switch to enable Socket Mode.
   - Click **"Generate Token"** to create a new Socket Mode token. Copy this token; you'll need it later.

4. **Create a Slash Command**:
   - In the left sidebar, click on **"Slash Commands"**.
   - Click **"Create New Command"**.
   - Fill in the following details:
     - **Command**: `/test_form`
     - **Request URL**: Leave this blank for now.
     - **Short Description**: `Test form command`
     - **Usage Hint**: `(optional)`
   - Click **"Save"**.

5. Enable Interactivity & Shortcuts
 - In the left sidebar, click on **"Interactivity & Shortcuts"**.
 - Toggle the switch to enable it

6. Enable Event Subscriptions
 - In the left sidebar, click on **"Event Subscriptions"**.
 - Toggle the switch to enable it
 - Subscribe to these bot events below in the section to subscribe to bot events
    - app_mention
    - message.channels
    - message.groups
    - message.im
 - Click on the save button below

---

## Installing Required Tools

1. **Install Python**:
   - If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Required Python Packages**:
   - Open your terminal or command prompt.
   - Run the following commands to install the necessary Python packages:
     ```bash
     pip install slack-bolt python-dotenv
     ```

---

## Setting Up the Environment

1. **Create a `.env` File**:
   - In the same folder where your `app.py` file is located, create a new file named `.env`.
   - Open the `.env` file in a text editor and add the following lines:
     ```
     SLACK_BOT_TOKEN=xoxb-your-bot-token
     SLACK_APP_TOKEN=xapp-your-app-token
     CHANNEL_ID=your-channel-id
     ```
   - Replace `xoxb-your-bot-token` with the **Bot User OAuth Token** you copied earlier.
   - Replace `xapp-your-app-token` with the **Socket Mode Token** you copied earlier.
   - Replace `your-channel-id` with the ID of the Slack channel where you want the bot to send messages. You can find the channel ID by right-clicking on the channel name in Slack and selecting **"Copy link"**. The channel ID is the part of the URL that looks like `C1234567890`.

2. **Save the `.env` File**:
   - Make sure to save the `.env` file after adding the tokens.

---

## Running the Bot

1. **Navigate to the Project Folder**:
   - Open your terminal or command prompt.
   - Use the `cd` command to navigate to the folder where your `app.py` file is located. For example:
     ```bash
     cd path/to/your/project/folder
     ```

2. **Run the Bot**:
   - In the terminal, run the following command to start the bot:
     ```bash
     python app.py
     ```
   - If everything is set up correctly, you should see a message saying `Starting Socket Mode Handler`.

---

## Testing the Bot

1. **Open Slack**:
   - Go to your Slack workspace where you installed the bot.

2. **Use the Slash Command**:
   - In any channel or direct message, type `/test_form` and press Enter.
   - The bot should respond with a form for you to fill out.

3. **Fill Out the Form**:
   - Fill out the form with the required information.
   - Click the **"Confirm&Forward"** button.

4. **Check the Output**:
   - The bot will send the filled-out form data to the specified channel (the one you set in the `CHANNEL_ID` variable).
   - You should also see a confirmation message in the channel where you used the `/test_form` command.

---

## Troubleshooting

- **Bot Not Responding**: Ensure that the bot is running in your terminal and that you have the correct tokens in the `.env` file.
- **Permission Errors**: Double-check that you added the correct scopes in the Slack app settings.
- **Channel ID Issues**: Make sure the `CHANNEL_ID` is correct and that the bot has permission to post in that channel.

---

## Conclusion

Congratulations! You've successfully set up and run the Slack bot. You can now use the `/test_form` command to collect and forward information within your Slack workspace. If you have any questions or run into issues, feel free to reach out for help.


