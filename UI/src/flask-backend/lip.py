import subprocess
import os

def convert_ogg_to_wav(input_path, output_path):
    try:
        ffmpeg_cmd = [
            'ffmpeg', '-y', '-i', input_path,
            '-ar', '44100', '-ac', '1', '-sample_fmt', 's16', output_path
        ]
        result = subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True)
        print(f"[INFO] FFmpeg Output: {result.stdout}")
        print(f"[INFO] Converted {input_path} to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] FFmpeg conversion failed: {e}")
        print(f"[ERROR] FFmpeg Output: {e.output}")
        print(f"[ERROR] FFmpeg Error: {e.stderr}")
        return False
    return True

def convert_wav_to_ogg(input_path, output_path):
    try:
        ffmpeg_cmd = [
            'ffmpeg', '-y', '-i', input_path, '-c:a', 'libvorbis', output_path
        ]
        result = subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True)
        print(f"[INFO] FFmpeg Output: {result.stdout}")
        print(f"[INFO] Converted {input_path} to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] FFmpeg conversion failed: {e}")
        print(f"[ERROR] FFmpeg Output: {e.output}")
        print(f"[ERROR] FFmpeg Error: {e.stderr}")
        return False
    return True

def run_rhubarb(input_wav, output_json):
    try:
        rhubarb_cmd = [
            'D:\\Git\\Sucide_Mitigation_Chatbot\\UI\\Rhubarb-Lip-Sync-1.13.0-Windows\\rhubarb.exe',
            '-f', 'json', input_wav, '-o', output_json
        ]
        result = subprocess.run(rhubarb_cmd, check=True, capture_output=True, text=True)
        print(f"[INFO] Rhubarb Output: {result.stdout}")
        print(f"[INFO] Rhubarb Error (if any): {result.stderr}")
        print(f"[INFO] Rhubarb processed {input_wav} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Rhubarb failed: {e}")
        print(f"[ERROR] Rhubarb Output: {e.output}")
        print(f"[ERROR] Rhubarb Error: {e.stderr}")
        return False
    return True

if __name__ == "__main__":
    ogg_file = "D:/Git/Sucide_Mitigation_Chatbot/UI/public/audios/output.ogg"
    wav_file = "D:/Git/Sucide_Mitigation_Chatbot/UI/public/audios/output_fixed.wav"
    reconverted_ogg = "D:/Git/Sucide_Mitigation_Chatbot/UI/public/audios/output_reconverted.ogg"
    json_output = "D:/Git/Sucide_Mitigation_Chatbot/UI/public/audios/output.json"
    
    if not os.path.exists(ogg_file):
        print(f"[ERROR] Input OGG file not found: {ogg_file}")
    else:
        if convert_ogg_to_wav(ogg_file, wav_file):
            if convert_wav_to_ogg(wav_file, reconverted_ogg):
                if run_rhubarb(wav_file, json_output):
                    print(f"[SUCCESS] JSON file created at {json_output}")
                else:
                    print("[ERROR] Rhubarb processing failed.")