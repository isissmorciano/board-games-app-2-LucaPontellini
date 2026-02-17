# Importiamo la funzione create_app dal pacchetto 'app'
# Questo è possibile perché 'app' ha un file __init__.py!
from setup_db import setup_database
from app import create_app

# Prima crea il database (solo se non esiste) setup_database()
setup_database()

# Chiamiamo la fabbrica per ottenere l'applicazione
app = create_app()

# Se questo file viene eseguito direttamente (non importato), avvia il server
if __name__ == "__main__":
    app.run(debug=True)