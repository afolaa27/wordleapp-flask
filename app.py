from flask import Flask,jsonify, g
from flask_cors import CORS
import models


DEBUG = True 
PORT = 8000


app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'], supports_credentials=True)

@app.route("/members", methods=['GET'])
def members():
	return jsonify(
		data="Member",
		message = "testing"

		)

if __name__ == "__main__":
	app.run(debug=DEBUG, port=PORT)