from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("myproject6-home.html")

@app.route("/api/v1/<word>")
def about(word):
    definition = word.upper()
    return {"definition": definition,
            "word": word}
    
if __name__ == "__main__":
    app.run(debug=True)