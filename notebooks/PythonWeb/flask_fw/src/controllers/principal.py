from flask import Blueprint
from flask import render_template


principal = Blueprint("principal", __name__, template_folder="templates")


@principal.route("/")
def documentation():
    return render_template("app/index.html")
