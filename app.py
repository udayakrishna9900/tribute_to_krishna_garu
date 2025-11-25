from flask import Flask, render_template

# Tell Flask exactly where templates and static files are
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Home page -> templates/index.html
@app.route("/")
def home():
    return render_template("index.html")

# About page -> templates/about.html
@app.route("/about")
def about():
    return render_template("about.html")

# Achievements page -> templates/achievements.html
@app.route("/achievements")
def achievements():
    return render_template("achievements.html")

# Gallery page -> templates/gallery.html
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


# Used only when running on your own laptop
if __name__ == "__main__":
    app.run(debug=False)
