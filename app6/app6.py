from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)
# execute only if run from this script
# why - because we may want to use only certain elements
# from this app in another project and not to run this whole script 
# as an argument we can add port=5001
# that is used when we have to apps in order for them not to
# crash, we execute them on diff ports (default is 5000)
