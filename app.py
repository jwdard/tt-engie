"""
Synthesis of the technical exercice:
JSON body with ASCII characters
Use pandas to return a JSON RESPONSE with a list of integers below H or h ASCII chracter code * 10 or 0
Return an 200 response with json result
"""
from flask import Flask
from flask import Blueprint, request, make_response
from converter import use

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/convert', methods=['POST'])
def convert():
    """post function
    """
    return make_response(use(request.get_json()), 200) 

def create_app() -> Flask:
    """create a flask app instance
    """

    flask_app = Flask('ml_api')

    flask_app.register_blueprint(prediction_app)

    return flask_app

application = create_app()

if __name__ == '__main__':
    application.run()