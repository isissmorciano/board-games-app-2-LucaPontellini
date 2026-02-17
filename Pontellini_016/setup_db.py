import sqlite3
import os

def setup_database():
    # Crea la cartella instance se non esiste
    if not os.path.exists("instance"):
        os.makedirs("instance")

    db_path = os.path.join("instance", "db.sqlite")

    # Se il DB esiste già, non lo ricrea
    if os.path.exists(db_path):
        print("Database già esistente, nessuna azione necessaria.")
        return

    # Crea il DB
    connection = sqlite3.connect(db_path)

    # Applica lo schema
    with open("app/schema.sql") as f:
        connection.executescript(f.read())

    print("Database creato con successo in:", db_path)
    connection.close()