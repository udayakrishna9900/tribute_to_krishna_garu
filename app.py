from flask import Flask, render_template

# create the Flask app
app = Flask(__name__)

# home page  -> templates/index.html
@app.route("/")
def home():
    return render_template("index.html")

# about page -> templates/about.html
@app.route("/about")
def about():
    return render_template("about.html")

# achievements page -> templates/achievements.html
@app.route("/achievements")
def achievements():
    return render_template("achievements.html")

# gallery page -> templates/gallery.html
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


# this part is only used when you run on your own laptop
if __name__ == "__main__":
    app.run(debug=False)

