from flask import Flask, request, jsonify
import slackapp
import logging
import threading

app = Flask(__name__)

# Start the slack app in a separate thread.
thread = threading.Thread(target=slackapp.start_slack_app)
thread.daemon = True
thread.start()

@app.route('/slack/events', methods=['POST'])
def slack_events_endpoint():
    try:
        data = request.get_json()
        if not data:
            return "No JSON data provided", 400

        # Process the data and send it to Slack
        try:
            print("Json data sent to slack app")
            slackapp.send_data_to_slack(data)
            return "Data sent to Slack", 200
        except Exception as e:
            logging.error(f"Error processing webhook data: {e}")
            return "Error processing webhook data", 500
    except Exception as e:
        logging.error(f"Error getting json data: {e}")
        return "Error getting json data", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
    