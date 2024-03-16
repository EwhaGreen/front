from flask import Flask, render_template
from database import DBhandler
import sys

application = Flask(__name__)
application.config["SECRET_KEY"] = "greenpower"
DB = DBhandler()

@application.route("/")
def hello():
    return render_template("main.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0')