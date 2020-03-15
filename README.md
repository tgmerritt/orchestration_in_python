### Explanation

Communicating with a UneeQ Digital Human requires an orchestration layer which serves to translate a user's request to the digital human to the customer's Natural Language Processing layer.  Orchestration basically serves as a JSON formatter, taking a payload which is POSTed from UneeQ's platform into the orchestration, transforming it into JSON appropriate for the target NLP, and then formatting the response from the NLP back into the JSON format expected by the UneeQ platform.

### Sample project includes Flask

In this particular sample, a entire orchestration layer has been setup including a light-weight web service powered by Flask.  This project could be deployed "as-is" to some web host, with the additional requirement of creating a hostname and adding a valid SSL certificate.  Once deployed, this particular project will simply repeat whatever question is input from the user right back to the user.  It acts as an echo in other words.  

### Where to add custom NLP

In ```orchestration.py```, there is a function called ```make_request``` which has been stubbed for your convenience as the starting point for custom NLP implementation.  There are a number of libraries in Python to make [HTTP requests](https://www.geeksforgeeks.org/get-post-requests-using-python/)

This project has a connection already with Google's Dialogflow and has been designed to process requests from that NLP engine that include UneeQ-specific tags such as emotionalTone and expressionEvent.  If you are using Google Dialogflow, you can simply add your json credentials file into the root of this project and deploy it to a service that will run Flask.  It should automatically work with your Dialogflow instance, and you should test this using a tool like Postman.

### Run tests

You can run the tests using ```python -m pytest -s -vv tests/```

You may need to install the libraries such as pytest, flask, etc., but if this is not your first Python application you may already have these installed.  But if not...

```
pip install flask pytest requests
```

In one terminal, from the root of the project:
```
export FLASK_ENV=development FLASK_APP=orchestration.py
flask run
```

This starts the flask server running the orchestration.py file, it's effectively now a webservice listening for requests on localhost:5000

Next open a new shell and navigate to the same project folder:
```
python -m pytest -s -vv tests/
```

### No Warranty

This is a sample project, and the code is delivered as-is.  No support or warranty, express or implied, is extended to this repository or any fork.  You are responsible for the implementation and maintenance of this code should you choose to use it in any capacity.  Resources permitting, we are happy to answer questions related to orchestration design.
