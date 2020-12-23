import unittest
from mock import patch
import json
from .. import google_dialog
# import ipdb
# ipdb.set_trace() to set a breakpoint for debugging
# Use the ! operator before any python statement inside the ipdb console, i.e. !print(response)


def new_send_query_to_dialogflow():
    return {'queryText': 'ねこ', 'parameters': {'pets': '猫'}, 'allRequiredParamsPresent': True, 'fulfillmentText': '<speak>かしこまりました。<say-as interpret-as="date">2020-03-03T12:00:00-06:00</say-as>の<say-as interpret-as="time">16:05:00</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>', 'fulfillmentMessages': [{'text': {'text': ['<speak>かしこまりました。<say-as interpret-as="date">2020-03-03T12:00:00-06:00</say-as>の<say-as interpret-as="time">16:05:00</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>']}}], 'outputContexts': [
        {'name': 'projects/newagent-gjetnk/agent/sessions/avatarSessionId/contexts/jpdemoconversation-kiohre.pet-chosen', 'lifespanCount': 5, 'parameters': {'pets': '猫', 'pets.original': 'ねこ'}}, {'name': 'projects/newagent-gjetnk/agent/sessions/avatarSessionId/contexts/__mega_agent_context__', 'lifespanCount': 2, 'parameters': {'pets': '猫', '__most_recent_agent_ids__': ['cc5655bc-2221-41fa-b956-cb0ab0929a5e, cc5655bc-2221-41fa-b956-cb0ab0929a5e'], 'pets.original': 'ねこ'}}], 'intent': {'name': 'projects/jpdemoconversation-kiohre/agent/intents/f32c1db0-fb20-4b9d-a64b-73dee7d5473a', 'displayName': 'jpdemo.conversation.pet-chosen'}, 'intentDetectionConfidence': 1, 'languageCode': 'ja'}


def html_send_query():
    return {
        'queryText': 'はい',
        'action': 'jpdemoconversationdestination.jpdemoconversationdestination-yes',
        'parameters': {
            'displayHtml': '<img src="assets/reserve_seat_list_select.png" style="margin-top: 3.5em;max-width: 300px;margin-right: 6em;" />',
            'emotionalTone': '[{"tone":"sadness","start":0.1, "value":1,"additive":false,"duration":10}]',
            'expressionEvent': '[{"expression":"smile","start":1, "value":1,"duration":10}]'
        },
        'allRequiredParamsPresent': True,
        'fulfillmentText': '承知致しました。席の空き状況はこちらです。ご希望の席をおっしゃって下さい。',
        'fulfillmentMessages': [
            {
                'text': {
                    'text': [
                        '承知致しました。席の空き状況はこちらです。ご希望の席をおっしゃって下さい。'
                    ]
                }
            }
        ],
        'outputContexts': [
            {
                'name': 'projects/jpdemoconversation-kiohre/agent/sessions/806544e0-1d27-3cf2-377d-2222953ffd0e/contexts/jp-train-demo',
                'lifespanCount': 5,
                'parameters': {
                    'date-period': '',
                    'time-period.original': '',
                    'date.original': '',
                    'destination_station': '新大阪駅',
                    'emotionalTone': '[{"tone":"sadness","start":0.1, "value":1,"additive":false,"duration":10}]',
                    'time': '2020-02-28T08:00:00-06:00',
                    'date': '2021-02-12T12:00:00-06:00',
                    'number': 2,
                    'time-period': '',
                    'emotionalTone.original': '',
                    'displayHtml.original': '',
                    'destination_station.original': '大阪',
                    'displayHtml': '<img src="assets/reserve_seat_list_select.png" style="margin-top: 3.5em;max-width: 300px;margin-right: 6em;" />',
                    'date-period.original': '',
                    'number.original': '２',
                    'time.original': '',
                    'originating_station.original': '',
                    'people.original': '',
                    'originating_station': '博多駅',
                    'people': 2
                }
            },
            {
                'name': 'projects/jpdemoconversation-kiohre/agent/sessions/806544e0-1d27-3cf2-377d-2222953ffd0e/contexts/jpdemoconversationdestination-followup',
                'lifespanCount': 5,
                'parameters': {
                    'people.original': '',
                    'originating_station.original': '',
                    'originating_station': '博多駅',
                    'people': 2,
                    'date.original': '',
                    'destination_station': '新大阪駅',
                    'time': '2020-02-28T08:00:00-06:00',
                    'date': '2021-02-12T12:00:00-06:00',
                    'displayHtml.original': '',
                    'displayHtml': '<img src="assets/reserve_seat_list_select.png" style="margin-top: 3.5em;max-width: 300px;margin-right: 6em;" />',
                    'destination_station.original': '大阪',
                    'time.original': ''
                }
            },
            {
                'name': 'projects/jpdemoconversation-kiohre/agent/sessions/806544e0-1d27-3cf2-377d-2222953ffd0e/contexts/passengers_selected',
                'lifespanCount': 4,
                'parameters': {
                    'displayHtml.original': '',
                    'destination_station.original': '大阪',
                    'displayHtml': '<img src="assets/reserve_seat_list_select.png" style="margin-top: 3.5em;max-width: 300px;margin-right: 6em;" />',
                    'number.original': '２',
                    'time.original': '',
                    'people.original': '',
                    'originating_station.original': '',
                    'originating_station': '博多駅',
                    'people': 2,
                    'date.original': '',
                    'destination_station': '新大阪駅',
                    'time': '2020-02-28T08:00:00-06:00',
                    'date': '2021-02-12T12:00:00-06:00',
                    'number': 2
                }
            },
            {
                'name': 'projects/jpdemoconversation-kiohre/agent/sessions/806544e0-1d27-3cf2-377d-2222953ffd0e/contexts/date_and_time_selected',
                'lifespanCount': 4,
                'parameters': {
                    'originating_station.original': '',
                    'people.original': '',
                    'originating_station': '博多駅',
                    'people': 2,
                    'date-period': '',
                    'time-period.original': '',
                    'date.original': '',
                    'destination_station': '新大阪駅',
                    'emotionalTone': '[{"tone":"sadness","start":0.1, "value":1,"additive":false,"duration":10}]',
                    'time': '2020-02-28T08:00:00-06:00',
                    'date': '2021-02-12T12:00:00-06:00',
                    'emotionalTone.original': '',
                    'time-period': '',
                    'number': 2,
                    'displayHtml.original': '',
                    'destination_station.original': '大阪',
                    'displayHtml': '<img src="assets/reserve_seat_list_select.png" style="margin-top: 3.5em;max-width: 300px;margin-right: 6em;" />',
                    'date-period.original': '',
                    'number.original': '２',
                    'time.original': ''
                }
            },
            {
                'name': 'projects/jpdemoconversation-kiohre/agent/sessions/806544e0-1d27-3cf2-377d-2222953ffd0e/contexts/destination_selected',
                'lifespanCount': 1,
                'parameters': {
                    'date.original': '',
                    'destination_station': '新大阪駅',
                    'time': '2020-02-28T08:00:00-06:00',
                    'date': '2021-02-12T12:00:00-06:00',
                    'displayHtml.original': '',
                    'displayHtml': '<img src="assets/reserve_seat_list_select.png" style="margin-top: 3.5em;max-width: 300px;margin-right: 6em;" />',
                    'destination_station.original': '大阪',
                    'time.original': '',
                    'people.original': '',
                    'originating_station.original': '',
                    'people': 2,
                    'originating_station': '博多駅'
                }
            }
        ],
        'intent': {
            'name': 'projects/jpdemoconversation-kiohre/agent/intents/62f9eff4-5933-47f2-94a3-8012073ffc01',
            'displayName': 'jpdemo.conversation.destination - yes'
        },
        'intentDetectionConfidence': 1,
        'languageCode': 'ja'
    }


class TestGoogleDialog(unittest.TestCase):

    def test_parse_with_time_and_date(self):
        gd = google_dialog.GoogleDialog(
            {}, "blah", "632c2f78-ca23-4cc2-8c1a-ad8e2403ca64")
        text = '<speak>かしこまりました。<say-as interpret-as="date">2020-03-03T12:00:00-06:00</say-as>の<say-as interpret-as="time">16:05:00</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>'
        parsed = gd.parse_fulfillment_text(text)
        assert parsed == '<speak>かしこまりました。<say-as interpret-as="date">2020-03-03</say-as>の<say-as interpret-as="time">16:05</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>'

    def test_no_speak_tag(self):
        gd = google_dialog.GoogleDialog(
            {}, "blah", "632c2f78-ca23-4cc2-8c1a-ad8e2403ca64")
        text = 'かしこまりました。'
        parsed = gd.parse_fulfillment_text(text)
        assert parsed == 'かしこまりました。'

    def test_parse_with_speak_tag_only(self):
        gd = google_dialog.GoogleDialog(
            {}, "blah", "632c2f78-ca23-4cc2-8c1a-ad8e2403ca64")
        text = '<speak>かしこまりました。</speak>'
        parsed = gd.parse_fulfillment_text(text)
        assert parsed == '<speak>かしこまりました。</speak>'

    # https://myadventuresincoding.wordpress.com/2011/02/26/python-python-mock-cheat-sheet/amp/
    @patch.object(google_dialog.GoogleDialog, 'send_query_to_dialogflow')
    def test_send_query_to_dialogflow(self, mock_send_query_to_dialogflow):
        def side_effect():
            return new_send_query_to_dialogflow()

        mock_send_query_to_dialogflow.side_effect = side_effect

        gd = google_dialog.GoogleDialog(
            {}, "blah", "632c2f78-ca23-4cc2-8c1a-ad8e2403ca64")
        response = gd.query_dialogflow()
        assert response == {
            'answer': '{"answer":"<speak>かしこまりました。<say-as interpret-as=\\"date\\">2020-03-03</say-as>の<say-as interpret-as=\\"time\\">16:05</say-as>でよろしいですね。空き状況を確認します。しばらくお待ち下さい。</speak>","instructions":{}}', 'matchedContext': '', 'conversationPayload': ''}

    @patch.object(google_dialog.GoogleDialog, 'send_query_to_dialogflow')
    def test_send_query_with_html(self, mock_send_query_to_dialogflow):
        def side_effect():
            return html_send_query()

        mock_send_query_to_dialogflow.side_effect = side_effect

        gd = google_dialog.GoogleDialog(
            {}, "blah", "632c2f78-ca23-4cc2-8c1a-ad8e2403ca64")
        response = gd.query_dialogflow()
        r = json.loads(response['answer'])
        assert r['answer'] == "承知致しました。席の空き状況はこちらです。ご希望の席をおっしゃって下さい。"
        assert r['instructions']['displayHtml'] == {
            'html': '<img src="assets/reserve_seat_list_select.png" style="margin-top: 3.5em;max-width: 300px;margin-right: 6em;" />'}
        assert r['instructions']['expressionEvent'] == [
            {"expression": "smile", "start": 1, "value": 1, "duration": 10}]
        assert r['instructions']['emotionalTone'] == [
            {"tone": "sadness", "start": 0.1, "value": 1, "additive": False, "duration": 10}]
