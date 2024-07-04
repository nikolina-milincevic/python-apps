from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
# giving __name__ as an argument allows me 
# to use templates relative to the directory
# where my python file is
# however, that doesn't hold for the files i'm opening

stations = pd.read_csv("app6/data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "app6/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)
