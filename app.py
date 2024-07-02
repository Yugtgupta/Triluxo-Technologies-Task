from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class ConversationHandler(Resource):
    def post(self):
        # Extract the conversation input from the request
        data = request.get_json()
        user_input = data.get('input', "what are some of the courses offered by brainlox")

        # Process the input (for demonstration, we'll just echo it back)
        response = {
            'response': f"Echoing your input: {user_input}"
        }
        return response, 200

# Add the ConversationHandler resource to our API
api.add_resource(ConversationHandler, '/conversation')

if __name__ == '__main__':
    app.run(debug=True)  # This line was missing. It starts the Flask application.