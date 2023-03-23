from flask import Flask, request
from gevent.pywsgi import WSGIServer
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_youtube_url():
    url = request.form.get('url')
    ydl_opts = {
        'format': 'worstaudio',
    }
    try:
        result = yt_dlp.YoutubeDL(ydl_opts).extract_info(url, download=False)
        response = {
            'status': 'ok',
            'url': result['url']
        }
        return response
    except Exception as e:
        response = {
            'status': 'error',
            'error': f'{e}'
        }
        return response

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()
