from flask import Flask, request, jsonify, render_template
import yt_dlp
import os

app = Flask(__name__)

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'noplaylist': True,  # Ensure only a single video is processed
        'format': 'best',  # Selects the best available format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            video_link = info.get("url")  # Get direct video URL
            return video_link
        except Exception as e:
            return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    video_link = get_video_info(url)

    if not video_link:
        return jsonify({"error": "No video link found"}), 400

    return jsonify({"video_link": video_link})

import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Get Railway-assigned PORT, default to 8080
    app.run(host="0.0.0.0", port=port)
