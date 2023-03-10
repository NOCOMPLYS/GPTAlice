import openai, logging
from flask import Flask, request, make_response
import json

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Define your Flask route
@app.route('/', methods=['POST'])
def resp():
    print('Request income!')
    text = request.json['request']['command']
    response_text = f'Вы сказали {text}'
    response = {
        "response": {
            "text": response_text,
            "end_session": False
        },
        "version": "1.0",
        "session": request.json['session']
    }
    
    return make_response(response, 200)

@app.route('/', methods=['GET'])
def hw():
    return "Hello, World!"

app.run(debug=True, host='0.0.0.0', port=5000, ssl_context="adhoc")


# Set up your OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
