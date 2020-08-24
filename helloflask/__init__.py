from flask import Flask, render_template, url_for, request,redirect
import speech_recognition as sr
from summarizer import Summarizer

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=["GET" , "POST"])
def upload():
    transcript=""
    result=""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            # transcript = recognizer.recognize_google(data, key=None)
            transcript = recognizer.recognize_sphinx(data)
            model = Summarizer()
            result = model(transcript)
            full = ''.join(result)
            print(full)
    return render_template('upload.html', result = result)

@app.route('/recording')
def recording():
    return render_template('recording.html')
