from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('data/events.json') as f:
        events = json.load(f)
    return render_template('events.html', events=events)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
