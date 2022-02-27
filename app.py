from flask import Flask
from flask_cors import CORS
import models


DEBUG = True 
PORT = 8000


app = Flask(__name__)

@app.route("/members")
	 
def members():
	return {"members": ["Member", "members2"]}

if __name__ == "__main__":
	app.run(debug=DEBUG, port=PORT)