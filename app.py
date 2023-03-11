import logging
from flask import Flask, request, make_response
import json

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Define your Flask route
@app.route('/', methods=['POST'])
def resp():
    event = request.json
    if 'request' in event and 'original_utterance' in event['request'] and len(event['request']['original_utterance']) > 0:
        user_id = event['session']['session_id']
        user_input = event['request']['original_utterance']
        response_text = "Вы сказали" + user_input
        return {
            'version': event['version'],
            'session': event['session'],
            'response': {
                'text': response_text,
                'tts': response_text,
                'end_session': False
            },
        }
    else:
        # If no input was provided, just return a welcome message
        return {
            'version': event['version'],
            'session': event['session'],
            'response': {
                'text': 'Джарвис на связи!',
                'tts': 'Джарвис на связи!',
                'end_session': False
            },
        }


app.run(debug=True, host='0.0.0.0', port=5000, ssl_context="adhoc")
