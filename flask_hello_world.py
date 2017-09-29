from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    return ("Hello World at " + str(datetime.datetime.now()))


if __name__ == "__main__":
    app.run()
