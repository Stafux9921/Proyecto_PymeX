# modelos/cliente.py

from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Representa un cliente final del servicio ISP.

    Coincide con la tabla 'clientes':
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre      TEXT NOT NULL,
        rut         TEXT NOT NULL,
        email       TEXT,
        telefono    TEXT
    """
    id: int | None
    nombre: str
    rut: str
    email: str
    telefono: str
