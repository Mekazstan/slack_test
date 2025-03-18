1. Goto https://api.slack.com/apps and create an APP with any name of your choice 
2. A selection box will pop up to to create the app (A)From Manifest or (B)From Scratch. Your are to choose create from scratch 
3. Next, you type in your desired app name [e.g. Forwarding service] and select the workspace you want it to work on (i.e. The workspace where the channels are located in) and then click on create an app.
4. So on the left side pane on the dashboard click on 


Copy Bot User OAuth Token from Installed App Settings [SLACK_BOT_TOKEN]
Copy Bot User OAuth Token from OAuth & Permissions [SLACK_APP_TOKEN]

-- Enable these Bot Token Scopes --
app_mentions:read
View messages that directly mention @Forward Service in conversations that the app is in

channels:history
View messages and other content in public channels that Forward Service has been added to

channels:join
Join public channels in a workspace

chat:write
Send messages as @Forward Service

chat:write.public
Send messages to channels @Forward Service isn't a member of

commands
Add shortcuts and/or slash commands that people can use

groups:history
View messages and other content in private channels that Forward Service has been added to

im:history
View messages and other content in direct messages that Forward Service has been added to

mpim:history
View messages and other content in group direct messages that Forward Service has been added to

5. Enable Interactivity & Shortcuts (Add URL)
6. Enable Event Subscriptions (Add URL)
Subscribe to these bot events
- app_mention
- message.channels
- message.groups
- message.im
7. Create Slash Commands
/Users/macbook2015/Downloads/Automation Series/Slack/slack-forward-bot.pub