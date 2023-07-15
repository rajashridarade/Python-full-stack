from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def demohello():
    return "welcome to flask app"

@app.route("/simple")
def other():
    return "it is very good,,lmkmmkmkm"


if __name__ == "__main__":
    app.run(debug=True,port=5500)
