import flask
from flask import request, jsonify
import logging
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/transcript', methods=['POST'])
def orchestrate():
    params = json.loads(request.data)
    print("Inbound request: {}".format(params))
    return make_request(params)


def make_request(params):
    # Implement your FETCH to remote NLP service here
    data = params  # data should be some JSON response from remote NLP, in our example, we will echo back the question we were asked, so we just set data equal to original params
    return create_json_to_send(data)


def create_json_to_send(data):
    # In our example, data is an empty object,
    answer_body = {
        "answer": data['fm-question'],
        "instructions": {
            "expressionEvent": [{}],
            "emotionalTone": [
                {
                    "tone": 'happiness',  # desired emotion in lowerCamelCase
                    "value": 0.2,  # number, intensity of the emotion to express between 0.0 and 1.0
                    "start": 2,  # number, in seconds from the beginning of the utterance to display the emotion
                    "duration": 4,  # number, duration in seconds this emotion should apply
                    # boolean, whether the emotion should be added to existing emotions (true), or replace existing ones (false)
                    "additive": False,
                    "default": True  # boolean, whether this is the default emotion
                }
            ]
            # "displayHtml": {
            #     "html": html
            # }
        }
    }

    body = {
        "answer": generate_json(answer_body),
        "matchedContext": '',
        "conversationPayload": generate_json({"sessionId": data['sid']})
    }
    return body


def generate_json(data):
    return json.dumps(data, separators=(',', ':'))


app.run()
