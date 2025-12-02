# modelos/empresa.py

from dataclasses import dataclass


@dataclass
class Empresa:
    """
    Representa una empresa ISP.

    Coincide con la tabla 'empresas':
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre          TEXT NOT NULL,
        rut             TEXT NOT NULL,
        email_contacto  TEXT
    """
    id: int | None
    nombre: str
    rut: str
    email_contacto: str
