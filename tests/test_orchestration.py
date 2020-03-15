import pytest
import requests
import json
import ipdb
# ipdb.set_trace() to set a breakpoint for debugging
# Use the ! operator before any python statement inside the ipdb console, i.e. !print(response)

url = 'http://127.0.0.1:5000'  # root URL of the app


class TestTransactions():
    def test_post_transcript(self):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'sid': "12345",
            'fm-question': "jp train demo start",
            'fm-custom-data': "",
            'fm-avatar': {"type": "WELCOME", "avatarSessionId": "632c2f78-ca23-4cc2-8c1a-ad8e2403ca64"}
        }

        result = requests.post(
            url+'/transcript', data=json.dumps(data), headers=headers)

        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'application/json'
        # The following assertion will *only* work for my original Dialogflow integration.  You should create an 'assert result.json() == WHATEVER_JSON' of your own
        # assert result.json() == {'answer': '{"answer":"<speak>いらしゃいませ！私はソフィーです。<break time=\\"3s\\"></break>新幹線のチケット予約をお手伝いします。出発の日を教えて下さい。</speak>","instructions":{"emotionalTone":[{"tone":"happiness","start":0.1,"value":0.9,"additive":true,"duration":5,"default":true}],"expressionEvent":[{"expression":"headPitch","value":-1,"start":1.9,"duration":3},{"expression":"eyePitch","value":-1,"start":1.9,"duration":3}]}}', 'conversationPayload': '', 'matchedContext': ''}
