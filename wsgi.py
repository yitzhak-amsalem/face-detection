from flask import Flask
from flask_cors import CORS

app = Flask('face_detection')
CORS(app, allow_headers='Content-Type')
app.run()
