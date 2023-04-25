import openai
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from flask import Flask, request, jsonify


# Set up the OpenAI API client with your API key
openai.api_key = "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"

# Define a function to generate a response to a user's message
#def generate_response(user_input, max_tokens=500):
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.1
    )

    # Extract the generated text from the OpenAI API response
    generated_text = response.choices[0].text

    return generated_text.strip()


# Create a Flask web server instance
app = Flask(__name__)


# Define a route for handling HTTP POST requests
@app.route("/", methods=["POST"])
def handle_post_request():
    # Extract the user input from the request payload
    user_input = request.json.get("message", "")

    # Generate a response to the user's input
    response = generate_response(user_input)

    # Return the response as a JSON object
    return jsonify({"message": response})


if __name__ == "__main__":
    # Start the Flask web server
    app.run(debug=True, port=8080)
