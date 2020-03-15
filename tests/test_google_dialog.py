import unittest
import mock
import json
import google_dialog


def new_send_query_to_dialogflow():
    return {'queryText': 'ねこ', 'parameters': {'pets': '猫'}, 'allRequiredParamsPresent': True, 'fulfillmentText': '<speak>かしこまりました。<say-as interpret-as="date">2020-03-03T12:00:00-06:00</say-as>の<say-as interpret-as="time">16:05:00</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>', 'fulfillmentMessages': [{'text': {'text': ['<speak>かしこまりました。<say-as interpret-as="date">2020-03-03T12:00:00-06:00</say-as>の<say-as interpret-as="time">16:05:00</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>']}}], 'outputContexts': [
        {'name': 'projects/newagent-gjetnk/agent/sessions/avatarSessionId/contexts/jpdemoconversation-kiohre.pet-chosen', 'lifespanCount': 5, 'parameters': {'pets': '猫', 'pets.original': 'ねこ'}}, {'name': 'projects/newagent-gjetnk/agent/sessions/avatarSessionId/contexts/__mega_agent_context__', 'lifespanCount': 2, 'parameters': {'pets': '猫', '__most_recent_agent_ids__': ['cc5655bc-2221-41fa-b956-cb0ab0929a5e, cc5655bc-2221-41fa-b956-cb0ab0929a5e'], 'pets.original': 'ねこ'}}], 'intent': {'name': 'projects/jpdemoconversation-kiohre/agent/intents/f32c1db0-fb20-4b9d-a64b-73dee7d5473a', 'displayName': 'jpdemo.conversation.pet-chosen'}, 'intentDetectionConfidence': 1, 'languageCode': 'ja'}


class TestGoogleDialog(unittest.TestCase):

    @mock.patch('google_dialog.GoogleDialog.send_query_to_dialogflow', side_effect=new_send_query_to_dialogflow)
    def test_send_query_to_dialogflow(self, send_query_to_dialogflow):
        gd = google_dialog.GoogleDialog(
            {}, "blah", "632c2f78-ca23-4cc2-8c1a-ad8e2403ca64")
        response = gd.query_dialogflow()
        print(response)
        assert response == {
            'answer': '{"answer":"<speak>かしこまりました。<say-as interpret-as=\\"date\\">2020-03-03</say-as>の<say-as interpret-as=\\"time\\">16:05</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>","instructions":{"expressionEvent":[{}],"emotionalTone":[{"tone":"happiness","value":0.2,"start":2,"duration":4,"additive":false,"default":true}]}}', 'matchedContext': '', 'conversationPayload': ''}

    def test_parse_fulfillment_text(self):
        gd = google_dialog.GoogleDialog(
            {}, "blah", "632c2f78-ca23-4cc2-8c1a-ad8e2403ca64")
        text = '<speak>かしこまりました。<say-as interpret-as="date">2020-03-03T12:00:00-06:00</say-as>の<say-as interpret-as="time">16:05:00</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>'
        parsed = gd.parse_fulfillment_text(text)
        assert parsed == '<speak>かしこまりました。<say-as interpret-as="date">2020-03-03</say-as>の<say-as interpret-as="time">16:05</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>'
