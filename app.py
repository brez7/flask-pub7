import os
from flask import Flask, render_template, request, send_from_directory, make_response

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


@app.route("/playground")
def playground():
    return render_template("playground.html", is_index=False)


@app.route("/dd")
def dd():
    return render_template("dd.html", is_index=False)


@app.route("/javascript")
def javascript():
    return render_template("javascript.html", is_index=False)


# Disable caching of static files by adding cache control headers
@app.route("/static/<path:filename>")
def static_files(filename):
    response = make_response(
        send_from_directory(os.path.join(app.root_path, "static"), filename)
    )
    response.headers["Cache-Control"] = (
        "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
    )
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "-1"
    return response


if __name__ == "__main__":
    server_port = os.environ.get("PORT", "8080")
    app.run(debug=True, port=server_port, host="0.0.0.0")
