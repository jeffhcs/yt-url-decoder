from flask import Flask, request
from gevent.pywsgi import WSGIServer
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_youtube_url():
    url = request.form.get('url')
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
            return result['url']
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()
