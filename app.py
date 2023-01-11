from flask import Flask, request, render_template
from stories import Story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route("/madlibs")
def get_answers():
    return render_template("form.html")

@app.route("/madlibs", methods=["POST"])
def print_madlib():
    response = request.form
    return render_template("story.html", show_story = story.generate(response))


    