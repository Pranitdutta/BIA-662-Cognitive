import requests
import json

# Define the URL endpoint for the HTTP server
url = 'http://localhost:8080/'

# Define the user input as a string
user_input = 'What are Electric vehicles?'

# Send an HTTP POST request to the server with the user input as a JSON payload
response = requests.post(url, json={'message': user_input})

# Extract the response message from the JSON response
response_message = response.json()['message']

# Print the response message
print(response_message)
