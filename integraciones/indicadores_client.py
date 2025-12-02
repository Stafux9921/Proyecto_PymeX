# integraciones/indicadores_client.py

"""
Cliente HTTP para consultar indicadores económicos desde una API externa.

Este módulo:
- Se conecta a la API (UF, Dólar, UTM, etc.)
- Obtiene los valores para una fecha dada
- Convierte los datos JSON en un objeto IndicadorEconomico (modelo del proyecto)

El objetivo de este cliente es aislar toda la lógica de solicitudes HTTP.
El repositorio NO debe hacer requests.
El servicio de indicadores usa este cliente.
"""

import requests
from datetime import date
from modelos.indicadores import IndicadorEconomico
from config import API_INDICADORES_BASE_URL


class IndicadoresClient:
    """
    Cliente para consumir la API de indicadores económicos.

    Usa requests.get() para obtener datos desde un endpoint externo.
    El formato exacto puede variar según la API usada.
    """

    def __init__(self, base_url: str = API_INDICADORES_BASE_URL):
        self.base_url = base_url.rstrip("/")

    def obtener_indicador(self, nombre: str, fecha: date) -> IndicadorEconomico:
        """
        Consulta la API externa para obtener un indicador económico para una fecha.

        Argumentos:
        - nombre: 'UF', 'DOLAR', 'UTM', etc.
        - fecha: datetime.date

        Retorna:
        - IndicadorEconomico (objeto del modelo)

        Lanza:
        - requests.exceptions.RequestException si la API falla
        - ValueError si la API no trae datos válidos
        """

        # Construir URL. Esto depende de la API real que uses.
        url = f"{self.base_url}/{nombre.upper()}/{fecha.isoformat()}"

        # Hacer request HTTP
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status()

        data = respuesta.json()

        # Según la API, el JSON puede ser distinto.
        # Aquí definimos un formato genérico esperado:
        # {
        #     "nombre": "UF",
        #     "fecha": "2025-01-10",
        #     "valor": 36000.12
        # }

        if "valor" not in data:
            raise ValueError(f"La API no devolvió un valor válido para {nombre} en {fecha}")

        return IndicadorEconomico(
            id=None,
            nombre=data["nombre"].upper(),
            fecha_valor=date.fromisoformat(data["fecha"]),
            valor=float(data["valor"])
        )
