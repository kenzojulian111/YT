from flask import Flask, request, render_template
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']  

    ydl_opts = {
        'format': 'bestvideo[height=720]',  
        'outtmpl': './Vi.mp4',           
    }

    try:
        # Proses unduhan
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Video successfully downloaded as Vi.mp4!"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
