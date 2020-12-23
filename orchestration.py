from flask import Flask, request, jsonify
import json
from . import google_dialog

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/transcript', methods=['POST'])
def orchestrate():
    params = json.loads(request.data)
    print("Inbound request: {}".format(params))
    return make_request(params)


def make_request(params):
    if 'fm-conversation' in params:
        conversation = params['fm-conversation']
    else:
        conversation = None
    gdf = google_dialog.GoogleDialog(conversation,
                                     params['fm-question'],
                                     params['fm-avatar']['avatarSessionId'])
    response = gdf.query_dialogflow()
    return response


if __name__ == "__main__":
    app.run()
