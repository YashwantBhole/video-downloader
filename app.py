from flask import Flask, request, jsonify, render_template
import yt_dlp

app = Flask(__name__)

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'noplaylist': True,  # Ensure only a single video is processed
        'format': 'best',  # Selects the best available format (single file)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_link = info.get("url")  # Get direct video URL
        return video_link

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        video_link = get_video_info(url)
        if not video_link:
            return jsonify({"error": "No video link found"}), 400

        return jsonify({"video_link": video_link})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
