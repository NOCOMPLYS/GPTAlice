import openai, logging, json
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Set up your OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define your Flask route
@app.route("/alice", methods=["POST"])
def main():
    text = request.json.get('request', {}).get('command')
    response_text = f'Вы сказали {text}'
    response = {
        "version": "1.0",
        #"session": request.json["session"],
        "response": {
            "text": response_text,
            "end_session": False
        }
    }
    
    return response



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

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
app.run(debug=True, host='0.0.0.0', port=5000, ssl_context="adhoc")
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')