from flask import Blueprint, render_template
from app.repositories import gioco_repository

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    # 1. Prendiamo i canali dal database
    giochi: list[dict] = gioco_repository.get_all_giochi()

    # 2. Passiamo la variabile 'giochi' al template
    return render_template("index.html", giochi=giochi)