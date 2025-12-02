# modelos/usuario.py

from dataclasses import dataclass
from enum import Enum


class RolUsuario(str, Enum):
    """
    Enum que representa los distintos roles que puede tener un usuario
    dentro del sistema.
    """
    CLIENTE = "cliente"
    EMPRESA = "empresa"
    ADMIN = "admin"


@dataclass
class Usuario:
    """
    Representa a un usuario del sistema.

    Coincide con la tabla 'usuarios':
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_usuario  TEXT NOT NULL UNIQUE,
        contrasena      TEXT NOT NULL,   -- hash de contraseña
        rol             TEXT NOT NULL
    """
    id: int | None
    nombre_usuario: str
    contrasena: str        # aquí se guarda el HASH, no el texto plano
    rol: RolUsuario
