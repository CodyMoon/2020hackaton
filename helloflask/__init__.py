from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': '첫 번째 아니아니',
        'content': '첫 번째 아니 내용입니다.',
        'date_posted': datetime.strptime('2018-08-01', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': '세 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-03', '%Y-%m-%d')
    },
]

@app.route('/')
def mainPage():
    return render_template('index.html', posts=posts)

@app.route('/index')
def index():
    return render_template('dropFile.html', title='File')

@app.route('/recording')
def recording():
  return render_template('recording.html', title='Recording')