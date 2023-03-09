import openai, logging, json
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Set up your OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define your Flask route
@app.route("/", methods=["POST"])
def main():
    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False
        }
    }

    req = request.json
    if req["session"]["new"]:
        response["responce"]["text"] = "Здравствуйте. Чем могу помочь?"
    
    return json.dumps(response)



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


if __name__ == '__main__':
    app.run(debug=True)
