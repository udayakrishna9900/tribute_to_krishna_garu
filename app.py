
from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__)

# Home page – shows templates/index.html
@app.route("/")
def home():
    return render_template("index.html")

# Optional extra routes if you use them:
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/achievements")
def achievements():
    return render_template("achievements.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

# Local run (not used on Render, but nice for your laptop)
if __name__ == "__main__":
    app.run(debug=False)
