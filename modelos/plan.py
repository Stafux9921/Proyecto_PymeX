# modelos/plan.py

from dataclasses import dataclass


@dataclass
class Plan:
    """
    Representa un plan de internet ofrecido por una empresa.

    Coincide con la tabla 'planes':
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa_id      INTEGER NOT NULL,
        nombre          TEXT NOT NULL,
        bajada_mbps     REAL NOT NULL,
        subida_mbps     REAL NOT NULL,
        contencion      INTEGER NOT NULL,   -- N de 1:N
        precio_clp      INTEGER NOT NULL,
        descripcion     TEXT
    """
    id: int | None
    empresa_id: int
    nombre: str
    bajada_mbps: float
    subida_mbps: float
    contencion: int
    precio_clp: int
    descripcion: str = ""
