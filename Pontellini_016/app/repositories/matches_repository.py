from app.db import get_db

def get_matches_by_game(game_id):
    db = get_db()
    query = """
        SELECT id, gioco_id, data, vincitore, punteggio_vincitore
        FROM partite
        WHERE gioco_id = ?
        ORDER BY data DESC
    """
    matches = db.execute(query, (game_id,)).fetchall()
    return [dict(m) for m in matches]


def get_match_by_id(match_id):
    db = get_db()
    query = """
        SELECT id, gioco_id, data, vincitore, punteggio_vincitore
        FROM partite
        WHERE id = ?
    """
    match = db.execute(query, (match_id,)).fetchone()
    return dict(match) if match else None


def create_match(game_id, data, vincitore, punteggio_vincitore):
    db = get_db()
    cursor = db.execute(
        """
        INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore)
        VALUES (?, ?, ?, ?)
        """,
        (game_id, data, vincitore, punteggio_vincitore)
    )
    db.commit()
    return cursor.lastrowid