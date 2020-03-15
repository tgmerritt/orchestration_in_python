import dialogflow_v2 as dialogflow
import json
from google.protobuf.json_format import MessageToJson
from dateutil.parser import parse
from bs4 import BeautifulSoup


class GoogleDialog:
    def __init__(self, state, query, session_id):
        self.state = state
        self.query = query
        self.session_id = session_id
        self.project_id = 'newagent-gjetnk'
        self.language_code = 'ja'

    def query_dialogflow(self):
        json_res = self.send_query_to_dialogflow()
        text = self.parse_fulfillment_text(json_res['fulfillmentText'])
        self.res = self.create_json_to_send(text)
        return self.res

    # By wrapping the dialogflow logic inside this function, we can mock it under test without having to worry about patching dialogflow functions
    def send_query_to_dialogflow(self):
        # Instantiate a new session and session_client from the dialogflow module
        session, session_client = self.return_new_session()
        # setup the text input object in advance of the dialogflow intent query
        text_input = dialogflow.types.TextInput(
            text=self.query, language_code=self.language_code)
        # Setup the final query object to dialogflow
        query_input = dialogflow.types.QueryInput(text=text_input)
        # Actually make the query to dialogflow using the detect_intent method and wait for response
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        # Render the QueryResult instance to JSON using the build in dialogflow JSON parser
        json_res = json.loads(MessageToJson(response.query_result))
        # Return the json response
        return json_res

    def return_new_session(self):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.project_id, self.session_id)
        return session, session_client

    # Sometimes the Dialogflow response may include SSML markup, in this case, we may need to format date and time values so they can be spoken properly
    def parse_fulfillment_text(self, text):
        if "<speak>" in text:
            b = BeautifulSoup(text, 'html.parser')
            if "interpret-as" in text:
                for e in b.find_all('say-as'):
                    if e['interpret-as'] == 'date':
                        date = parse(e.string)
                        e.string = str(date.date())
                    elif e['interpret-as'] == 'time':
                        # new_time = time.strptime(e.string, "%H:%M:%S")
                        # t = str(new_time.time()).split(":")
                        # print("t is now: {time}".format(time=t))
                        t = e.string.split(":")
                        e.string = t[0]+":"+t[1]
                    else:
                        pass
            print("This is the beautiful soup variable:")
            print(b)
            return str(b)
        else:
            return text

    # Build the JSON that we should return in response to the original POST
    def create_json_to_send(self, text):
        # In our example, data is an empty object,
        answer_body = {
            "answer": text,
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
            "answer": self.generate_json(answer_body),
            "matchedContext": '',
            "conversationPayload": ''
        }
        return body

    def generate_json(self, data):
        return json.dumps(data, separators=(',', ':'), ensure_ascii=False)
