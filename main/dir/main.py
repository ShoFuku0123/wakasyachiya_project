# 簡単なindexページの作成を行っています。
import os
from flask import Flask, render_template, request, send_from_directory
# from flask_migrate import Migrate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/audio_book")
def audio_book():
    return render_template('audio_book.html')

@app.route("/azumaya_top")
def azumaya_top():
    return render_template('azumaya_top.html')

@app.route('/audio/<filename>')
def get_audio(filename):
    """ MP3ファイルを提供するエンドポイント """
    return send_from_directory('static/audio', filename, mimetype='audio/mpeg')
