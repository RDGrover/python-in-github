import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r")as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)



@app.route("/about/<dwarf_name>")
def about_dwarf(dwarf_name):
    dwarf = {}
    with open("data/company.json", "r")as json_data:
        data = json.load(json_data)
        for object in data:
            if object["url"] == dwarf_name:
                dwarf = object
    return render_template("dwarf.html", dwarf=dwarf)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash(
            "We have heard your call {}.".format(request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
