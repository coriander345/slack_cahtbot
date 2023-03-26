import os
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
# Initialize the App with your bot token
app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

channel_id = "C04UF32E97Y"

@app.event("app_mention")
async def mention_handler(body, say):
    text = body['event']['text']
    print(text)

    if 'hello' in text.lower():
        await say('Hello! How can I help you today?')

s


# Set up the Flask app
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# Define the route for handling Slack events
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    flask_app.run(port=3000)
