import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.context_processor
def inject_styles():
    is_homepage = request.path == "/"
    # You can add more context variables as needed
    return dict(is_homepage=is_homepage)


@app.route("/")
def home():
    return render_template("index.html", is_index=True)


@app.route("/locations")
def locations():
    return render_template("locations.html", is_index=False)


@app.route("/menu")
def menu():
    return render_template("menu.html", is_index=False)


@app.route("/contact")
def contact():
    return render_template("contact.html", is_index=False)


@app.route("/about")
def about():
    return render_template("about.html", is_index=False)


@app.route("/dd")
def dd():
    return render_template("dd.html", is_index=False)


if __name__ == "__main__":
    server_port = os.environ.get("PORT", "8080")
    app.run(debug=False, port=server_port, host="0.0.0.0")
