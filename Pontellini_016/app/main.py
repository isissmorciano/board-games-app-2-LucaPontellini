from flask import Blueprint, render_template, request, redirect, url_for
from app.repositories import games_repository
from app.repositories import matches_repository

bp = Blueprint("main", __name__)


# Homepage
@bp.route("/")
def index():
    games = games_repository.get_all_games()
    return render_template("index.html", games=games)


# Lista giochi
@bp.route("/games")
def lista_giochi():
    games = games_repository.get_all_games()
    return render_template("games.html", games=games)


# Nuovo gioco
@bp.route("/games/new", methods=["GET", "POST"])
def nuovo_gioco():
    if request.method == "POST":
        nome = request.form["nome"]
        max_giocatori = request.form["numero_giocatori_massimo"]
        durata = request.form["durata_media"]
        categoria = request.form["categoria"]

        games_repository.create_game(nome, max_giocatori, durata, categoria)

        return redirect(url_for("main.lista_giochi"))

    return render_template("new_game.html")


# Lista partite
@bp.route("/games/<int:game_id>/matches")
def lista_partite(game_id):
    gioco = games_repository.get_game_by_id(game_id)
    partite = matches_repository.get_matches_by_game(game_id)
    return render_template("matches.html", gioco=gioco, partite=partite)


# Nuova partita
@bp.route("/games/<int:game_id>/matches/new", methods=["GET", "POST"])
def nuova_partita(game_id):
    if request.method == "POST":
        data = request.form["data"]
        vincitore = request.form["vincitore"]
        punteggio = request.form["punteggio_vincitore"]

        matches_repository.create_match(game_id, data, vincitore, punteggio)

        return redirect(url_for("main.lista_partite", game_id=game_id))

    return render_template("new_match.html", game_id=game_id)