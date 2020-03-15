import pytest
import requests
import json

url = 'http://127.0.0.1:5000'  # root URL of the app


class TestTransactions():
    def test_post_transcript(self):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'sid': "12345",
            'fm-question': "Do you like coffee?",
            'fm-custom-data': "",
            'fm-avatar': {"type": "WELCOME"}
        }

        result = requests.post(
            url+'/transcript', data=json.dumps(data), headers=headers)

        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'application/json'
        assert result.json() == {
            "answer": "{\"answer\":\"Do you like coffee?\",\"instructions\":{\"expressionEvent\":[{}],\"emotionalTone\":[{\"tone\":\"happiness\",\"value\":0.2,\"start\":2,\"duration\":4,\"additive\":false,\"default\":true}]}}",
            "conversationPayload": "{\"sessionId\":\"12345\"}",
            "matchedContext": ""
        }
