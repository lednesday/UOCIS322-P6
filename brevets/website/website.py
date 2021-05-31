from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('display_times.html')


@app.route('/listeverything')
def listeverything():
    r = requests.get('http://restapi:5000/listAll')
    return r.text


@app.route('/listopen')
def listopen():
    r = requests.get('http://restapi:5000/listOpenOnly')
    return r.text


@app.route('/listclose')
def listclose():
    r = requests.get('http://restapi:5000/listCloseOnly')
    return r.text


# @app.route('/listeverythingcsv')
# def listeverything():
#     r = requests.get('http://restapi:5000/listAll/csv')
#     return r.text


# @app.route('/listopencsv')
# def listeverything():
#     r = requests.get('http://restapi:5000/listOpenOnly/csv')
#     return r.text


# @app.route('/listclosecsv')
# def listeverything():
#     r = requests.get('http://restapi:5000/listCloseOnly/csv')
#     return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
