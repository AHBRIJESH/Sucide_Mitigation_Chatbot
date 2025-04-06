from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import shutil
import requests
import torch
import subprocess
import os
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the chatbot model
model_path = r"D:\Git\Sucide_Mitigation_Chatbot\model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)

# Eleven Labs API details
API_KEY = "sk_b5e5696ecf66a0c37de4476573d0036b8250a9f135208f66"
VOICE_ID = "pqHfZKP75CvOlQylNhV4"
TTS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
OUTPUT_AUDIO_PATH = "D:/Git/Sucide_Mitigation_Chatbot/output.ogg"
DESTINATION_PATH = "D:/Git/Sucide_Mitigation_Chatbot/UI/public/audios/output.ogg"
LIP_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "lip.py")  # Path to lip.py

app = Flask(__name__)
CORS(app)

def get_response(input_text):
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

def generate_speech(text):
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(TTS_URL, json=data, headers=headers)
    if response.status_code == 200:
        with open(OUTPUT_AUDIO_PATH, "wb") as file:
            file.write(response.content)
        return True
    else:
        print(f"Error generating speech: {response.status_code}, {response.text}")
        return False

def run_lip_sync():
    try:
        subprocess.Popen(["python", LIP_SCRIPT_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # Run in background
        print("[INFO] Started lip sync processing.")
    except Exception as e:
        print(f"[ERROR] Failed to start lip sync: {e}")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    sys.stdout.flush()

    bot_response = get_response(user_message)

    if generate_speech(bot_response):
        shutil.move(OUTPUT_AUDIO_PATH, DESTINATION_PATH)
        run_lip_sync()  # Just start lip.py and move on
        return jsonify({"response": bot_response, "audio_path": DESTINATION_PATH})
    else:
        return jsonify({"response": bot_response, "error": "Failed to generate speech"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)