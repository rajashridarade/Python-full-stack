from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello():
    uname = "RAJASHRI DARADE"
    return render_template("hello.html", username=uname)


@app.route("/display")
def display():
    fname = "Radjads"
    lname = "daada"
    return render_template("displayname.html", firstname=fname, lastname=lname)


@app.route("/displaylist")
def displaylist():
    data = ["hera", "meere", "nira"]
    return render_template("displaylist.html", data=data)


@app.route("/displaynlist")
def displaynlist():
    data = [[101, "hera", 23], [102, "meere", 22], [103, "nira", 12]]
    return render_template("displaynlist.html", data=data)


@app.route("/displaydict")
def displaydict():
    data = {101: "hera", 102: "meere", 103: "nira"}
    return render_template("displaydict.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
