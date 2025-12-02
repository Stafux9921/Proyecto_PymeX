# modelos/indicadores.py

from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class IndicadorEconomico:
    """
    Representa el valor de un indicador económico en una fecha dada.

    Coincide con la tabla 'indicadores':
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre          TEXT NOT NULL,   -- 'UF', 'DOLAR', 'UTM', etc.
        fecha_valor     TEXT NOT NULL,   -- 'YYYY-MM-DD'
        valor           REAL NOT NULL
    """
    id: int | None
    nombre: str
    fecha_valor: date
    valor: float


@dataclass
class ConsultaIndicador:
    """
    Representa el registro de una consulta de indicador hecha por un usuario.

    Coincide con la tabla 'consultas_indicadores':
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        indicador_id    INTEGER NOT NULL,
        usuario_id      INTEGER NOT NULL,
        fecha_consulta  TEXT NOT NULL,   -- 'YYYY-MM-DDTHH:MM:SS'
        fuente          TEXT NOT NULL
    """
    id: int | None
    indicador_id: int
    usuario_id: int
    fecha_consulta: datetime
    fuente: str
