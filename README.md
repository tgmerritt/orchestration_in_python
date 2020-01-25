### Explanation

Communicating with a UneeQ Digital Human requires an orchestration layer which serves to translate a user's request to the digital human to the customer's Natural Language Processing layer.  Orchestration basically serves as a JSON formatter, taking a payload which is POSTed from UneeQ's platform into the orchestration, transforming it into JSON appropriate for the target NLP, and then formatting the response from the NLP back into the JSON format expected by the UneeQ platform.

### Sample project includes Flask

In this particular sample, a entire orchestration layer has been setup including a light-weight web service powered by Flask.  This project could be deployed "as-is" to some web host, with the additional requirement of creating a hostname and adding a valid SSL certificate.  Once deployed, this particular project will simply repeat whatever question is input from the user right back to the user.  It acts as an echo in other words.  

### Where to add custom NLP

In ```orchestration.py```, there is a function called ```make_request``` which has been stubbed for your convenience as the starting point for custom NLP implementation.  There are a number of libraries in Python to make [HTTP requests](https://www.geeksforgeeks.org/get-post-requests-using-python/)

### No Warranty

This is a sample project, and the code is delivered as-is.  No support or warranty, express or implied, is extended to this repository or any fork.  You are responsible for the implementation and maintenance of this code should you choose to use it in any capacity.  Resources permitting, we are happy to answer questions related to orchestration design.