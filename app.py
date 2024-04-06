import os

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    send_file,
)

app = Flask(__name__)


@app.route("/")
def index():
    # return send_file("data/menu/Menu Goldis 1_page-0001.jpg")

    return redirect(url_for("menu"))


# @app.route("/menu1")
# def menu1():
#     print("Request for menu page 1 received")
#     return send_file("data/menu/Menu Goldis A1-combined.pdf")


# @app.route("/menu2")
# def menu2():
#     print("Request for menu page 2 received")

#     return send_file("data/menu/Menu Goldis A1-combined.pdf")


@app.route("/menu")
def menu():
    return render_template("menu.html")


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
