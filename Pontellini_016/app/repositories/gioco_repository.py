from app.db import get_db

def get_all_giochi():
    db = get_db()
    query = """
        SELECT gioco.id,
               gioco.nome,
               gioco.numero_iscritti,
               gioco.nome AS gioco
        FROM gioco
        JOIN gioco ON gioco.gioco_id = gioco.id
        ORDER BY numero_iscritti DESC
    """
    giochi = db.execute(query).fetchall()
    return [dict(gioco) for gioco in giochi]


def get_gioco_by_id(gioco_id):
    db = get_db()
    query = """
        SELECT gioco.id,
               gioco.nome,
               gioco.numero_iscritti,
               gioco.nome AS gioco,
               gioco.gioco_id
        FROM gioco
        JOIN gioco ON gioco.gioco_id = gioco.id
        WHERE gioco.id = ?
    """
    gioco = db.execute(query, (gioco_id,)).fetchone()
    return dict(gioco) if gioco else None


def create_channel(nome, numero_iscritti, gioco_id):
    db = get_db()
    cursor = db.execute(
        "INSERT INTO gioco (nome, numero_iscritti, gioco_id) VALUES (?, ?, ?)",
        (nome, numero_iscritti, gioco_id)
    )
    db.commit()
    return cursor.lastrowid