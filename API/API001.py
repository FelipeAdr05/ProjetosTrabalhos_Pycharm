from flask import Flask, jsonify, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<data>')

def dias_vida(data):
    tday = datetime.date.today()
    bday = datetime.date(int(data[6:10]), int(data[3:5]), int(data[:2]))
    qnt_days = tday - bday
    qnt_days = qnt_days.days
    return jsonify({'Qnt Dias': qnt_days})

app.run(host='0.0.0.0')