import random
import time
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    content = request.form['content']
    print(content)
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run()