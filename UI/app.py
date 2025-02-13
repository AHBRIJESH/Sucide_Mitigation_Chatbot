from flask import Flask, render_template, request, send_file, jsonify
import pyttsx3
import os

app = Flask(__name__)
AUDIO_FILE = "static/generated_audio.wav"
os.makedirs("static", exist_ok=True)

def text_to_speech(text, rate=200, filename=AUDIO_FILE):
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)  # ✅ Apply the speech rate
    engine.save_to_file(text, filename)
    engine.runAndWait()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def generate_audio():
    data = request.json
    text = data.get("text", "Hello! This is a test for text-to-speech waveform visualization.")  # Default text
    rate = data.get("rate", 200)  
    text_to_speech(text, rate)  # ✅ Pass rate to the function
    return jsonify({"audio_url": "/static/generated_audio.wav"})

@app.route("/audio")
def serve_audio():
    return send_file(AUDIO_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)