from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('display_times.html')


@app.route('/listeverything')
def listeverything():
    json_or_csv = request.args.get('format', "json", type=str)
    num_lines = request.args.get('lines', -1, type=int)
    r = requests.get(
        f'http://restapi:5000/listAll/{json_or_csv}?top={num_lines}')
    return r.text


@app.route('/listopen')
def listopen():
    json_or_csv = request.args.get('format', "json", type=str)
    num_lines = request.args.get('lines', -1, type=int)
    r = requests.get(
        f'http://restapi:5000/listOpenOnly/{json_or_csv}?top={num_lines}')
    return r.text


@app.route('/listclose')
def listclose():
    json_or_csv = request.args.get('format', "json", type=str)
    num_lines = request.args.get('lines', -1, type=int)
    r = requests.get(
        f'http://restapi:5000/listCloseOnly/{json_or_csv}?top={num_lines}')
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
