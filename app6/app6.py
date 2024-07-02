from flask import Flask, render_template

app = Flask("Website")

@app.route("/home")
def home():
    return render_template("tutorial.html")
# here, tutorial.html needs to be in a folder named templates
# because render_template() looks for this file in such folder
# but since in VSCode i openned python apps folder, then 
# my folder templates needs to be in that folder and 
# not in the folder app6

@app.route("/about/")
def about():
    return render_template("about.html")

app.run(debug=True)
