# db/init_db.py

"""
Inicializa la base de datos SQLite ejecutando el archivo schema.sql.

- Abre la base de datos ispplus.db en la raíz del proyecto.
- Lee el script SQL (schema.sql).
- Crea las tablas si no existen.
"""

import sqlite3
from pathlib import Path

# Directorio base del proyecto: carpeta padre de /db
BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta al archivo de base de datos SQLite
DB_PATH = BASE_DIR / "ispplus.db"


def init_db():
    """
    Ejecuta el script schema.sql para crear todas las tablas necesarias.
    """
    schema_path = Path(__file__).resolve().parent / "schema.sql"

    with sqlite3.connect(DB_PATH) as conn:
        with open(schema_path, "r", encoding="utf-8") as f:
            script = f.read()
            conn.executescript(script)
        conn.commit()

    print(f"Base de datos inicializada en: {DB_PATH}")
