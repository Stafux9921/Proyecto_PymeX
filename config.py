# config.py

"""
Configuración global del proyecto ISPPlus.

Aquí se definen constantes como:
- Ruta al archivo de base de datos SQLite.
- URLs base de APIs externas.
- Parámetros generales de la aplicación.
"""

from pathlib import Path

# Directorio base del proyecto (carpeta donde está config.py)
BASE_DIR = Path(__file__).resolve().parent

# Ruta al archivo de base de datos SQLite
DB_PATH = BASE_DIR / "ispplus.db"

# URL base de la API de indicadores económicos (ejemplo, reemplazar por la real)
API_INDICADORES_BASE_URL = "https://api.ejemplo.com/indicadores"

# Nombre de la aplicación (por si lo quieres mostrar en menús/títulos)
APP_NAME = "ISPPlus Backend"

# Puedes agregar más configuración aquí si la necesitas más adelante:
# - TIMEOUTS para requests
# - FLAGS de depuración
# - etc.
