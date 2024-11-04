from flask import Flask, request, jsonify
from flask_cors import CORS
from unalengua import Unalengua
import pronouncing

app = Flask(__name__)
CORS(app)


def get_transcription(word):
    phones = pronouncing.phones_for_word(word)
    if not phones:
        return []

    transcription = [{"character": char, "color": "blue"} for char in phones[0].split()]
    return transcription


@app.route("/api/transcription", methods=["POST"])
def transcription():
    data = request.json
    word = data.get("word", "").lower()
    transcription = get_transcription(word)

    if not transcription:
        return jsonify({"Error": "Word not found"}), 404

    return jsonify({"transcription": transcription})


if __name__ == "__main__":
    app.run(debug=True)
