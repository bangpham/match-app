from flask import render_template
from flask import Flask, jsonify
from business import time

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/time')
def get_time():
    time_obj = time.Time()
    return jsonify(time_obj.get_time())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
