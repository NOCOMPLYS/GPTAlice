import openai, logging, json
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Set up your OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define your Flask route
@app.route('/', methods=['POST'])
def main():
    logging.info(request.json)
    """
    response ={
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False
        }
    }

    req = request.json
    if req["session"]
    """


"""
def index():
    # Get the user's voice input
    audio_data = request.data

    # Convert the audio to text using OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=audio_data,
        max_tokens=60,
        temperature=0.5,
    )
    text = response.choices[0].text.strip()

    # Send the generated text back to the user
    return text
"""
if __name__ == '__main__':
    app.run(debug=True)

