import datetime
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def nYear():
    now = datetime.datetime.now()
    ny = now.month == 1 and now.day == 1
    return render_template("newyear.html",ny=ny)