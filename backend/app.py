from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/transcription", methods=["POST"])
def transcription():
    data = request.json
    word = data.get("word")

    transcription = [
        {"character": "h", "color": "green"},
        {"character": "ə", "color": "yellow"},
        {"character": "l", "color": "red"},
        {"character": "oʊ", "color": "yellow"},
    ]

    return jsonify({"transcription": transcription})


if __name__ == "__name__":
    app.run(debug=True)
