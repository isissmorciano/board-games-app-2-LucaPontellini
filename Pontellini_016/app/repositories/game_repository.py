from app.db import get_db

def get_all_games():
    db = get_db()
    query = """
        SELECT giochi.id,
               giochi.nome,
               giochi.numero_giocatori_massimo,
               giochi.durata_media,
               categoria.nome AS categoria
        FROM giochi
        JOIN categoria ON giochi.categoria_id = categoria.id
        ORDER BY numero_giocatori_massimo DESC
    """
    giochi = db.execute(query).fetchall()
    return [dict(gioco) for gioco in giochi]


def get_game_by_id(gioco_id):
    db = get_db()
    query = """
        SELECT giochi.id,
               giochi.nome,
               giochi.numero_giocatori_massimo,
               categoria.nome AS gioco,
               giochi.gioco_id
        FROM giochi
        JOIN categoria ON giochi.categoria_id = categoria.id
        WHERE giochi.id = ?
    """
    gioco = db.execute(query, (gioco_id,)).fetchone()
    return dict(gioco) if gioco else None


def create_game(nome, numero_giocatori_massimo, gioco_id):
    db = get_db()
    cursor = db.execute(
        "INSERT INTO giochi (nome, numero_giocatori_massimo, categoria_id) VALUES (?, ?, ?)",
        (nome, numero_giocatori_massimo, gioco_id)
    )
    db.commit()
    return cursor.lastrowid