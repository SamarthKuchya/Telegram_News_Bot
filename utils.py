import os
from google.cloud import dialogflow_v2beta1 as dialogflow

os.environ['GOOGLE_APPLICATION_CREDENTIALS']="client.json"
dialogflow_session_client=dialogflow.SessionsClient()
project_id="newsbot-mkqm"

def detect_intent_from_text(text,session_id,language_code='en'):
    session=dialogflow_session_client.session_path(project_id,session_id)
    text_input=dialogflow.types.TextInput(text=text,language_code=language_code)
    query_input=dialogflow.types.QueryInput(text=text_input)
    response=dialogflow_session_client.detect_intent(session=session,query_input=query_input)
    return response.query_result

from gnewsclient import gnewsclient
client=gnewsclient.NewsClient()

def fetch_news(parameters):
    # client.language=parameters.get('language')
    # client.location=parameters.get('geo-country')
    client.language='Hindi'
    client.location="India"
    client.topic=parameters.get('topic')
    return client.get_news()[:5]



def get_reply(query,chat_id):
    response=detect_intent_from_text(query,chat_id)

    if response.intent.display_name=='get_news':
        return "get_news",dict(response.parameters)
    else:
        return "small_talk",response.fulfillment_text
    
topic_keyboard=[
                 ['World','Nation','Business'],
                 ['Technology','Entertainment'],
                 ['Sports','Science','Health'],
                 ]