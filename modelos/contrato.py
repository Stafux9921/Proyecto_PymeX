# modelos/contrato.py

from dataclasses import dataclass
from datetime import date


@dataclass
class ContratoPlan:
    """
    Representa un contrato de un plan entre un cliente y una empresa.

    Coincide con la tabla 'contratos':
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id      INTEGER NOT NULL,
        plan_id         INTEGER NOT NULL,
        fecha_inicio    TEXT NOT NULL,   -- 'YYYY-MM-DD'
        fecha_fin       TEXT,
        estado          TEXT NOT NULL    -- 'activo', 'suspendido', 'terminado', ...
    """
    id: int | None
    cliente_id: int
    plan_id: int
    fecha_inicio: date
    fecha_fin: date | None
    estado: str
