import dialogflow_v2 as dialogflow
import json
from google.protobuf.json_format import MessageToJson
from dateutil.parser import parse
from bs4 import BeautifulSoup
# import ipdb
# ipdb.set_trace() to set a breakpoint for debugging
# Use the ! operator before any python statement inside the ipdb console, i.e. !print(response)


class GoogleDialog:
    def __init__(self, state, query, session_id):
        self.state = state
        self.query = query
        self.session_id = session_id
        self.project_id = 'newagent-gjetnk'
        self.language_code = 'ja'

    def query_dialogflow(self):
        self.dialog_flow_response = self.send_query_to_dialogflow()
        # ipdb.set_trace()
        text = self.parse_fulfillment_text(self.dialog_flow_response['fulfillmentText'])
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

    # Each dialogflow session holds the context of the conversation, so ensuring that we pass the correct session with our detectIntent liberates us from having to manually manage the context of each conversation
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
                        t = e.string.split(":")
                        e.string = t[0]+":"+t[1]
                    else:
                        pass
            return str(b)
        else:
            return text

    # If the user has passed emotionalTone or expressionEvent as parameters back from Dialogflow, add them to the instructions object
    def setup_instructions(self):
        instructions = {}
        if 'emotionalTone' in self.dialog_flow_response['parameters']:
            instructions['emotionalTone'] = json.loads(self.dialog_flow_response['parameters']['emotionalTone'])
        if 'expressionEvent' in self.dialog_flow_response['parameters']:
            instructions['expressionEvent'] = json.loads(self.dialog_flow_response['parameters']['expressionEvent'])
        if 'displayHtml' in self.dialog_flow_response['parameters']:
            instructions['displayHtml'] = self.generate_html()
        return instructions

    # The HTML property of the UneeQ response is slightly different from the emotionalTone and expressionEvent key-value pairs, so we set it up here
    def generate_html(self):
        return {'html': self.dialog_flow_response['parameters']['displayHtml']}

    # Build the JSON that we should return in response to the original POST
    def create_json_to_send(self, text):
        # In our example, data is an empty object,
        answer_body = {
            "answer": text,
            "instructions": self.setup_instructions()
        }

        body = {
            "answer": self.generate_json(answer_body),
            "matchedContext": '',
            "conversationPayload": ''
        }
        return body

    def generate_json(self, data):
        return json.dumps(data, separators=(',', ':'), ensure_ascii=False)
