from flask import Flask, request
import openai
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
   data = json.loads(request.data)
   print("New commit by: {}".format(data['commits'][0]['author']['name']))
   return "OK"

if __name__ == '__main__':
   app.run()



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