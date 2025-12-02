# servicios/plan_service.py

"""
Servicio de negocio para gestionar:
- Planes
- Contratos
"""

from datetime import date
from modelos.plan import Plan
from modelos.contrato import ContratoPlan
from repositorios.plan_repo import PlanRepositorio
from repositorios.contrato_repo import ContratoRepositorio


class PlanService:
    """
    Lógica empresarial relacionada a planes y contratos.
    """

    def __init__(self):
        self.repo_plan = PlanRepositorio()
        self.repo_contrato = ContratoRepositorio()

    # ---------------------------
    # PLANES
    # ---------------------------

    def crear_plan(self, empresa_id: int, nombre: str, bajada: float, subida: float,
                   contencion: int, precio: int, descripcion: str = "") -> Plan:
        """
        Crea un plan validando sus datos.
        """
        if bajada <= 0 or subida <= 0:
            raise ValueError("Las velocidades deben ser mayores a 0")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        nuevo = Plan(
            id=None,
            empresa_id=empresa_id,
            nombre=nombre,
            bajada_mbps=bajada,
            subida_mbps=subida,
            contencion=contencion,
            precio_clp=precio,
            descripcion=descripcion
        )

        return self.repo_plan.crear(nuevo)

    def listar_planes_empresa(self, empresa_id: int) -> list[Plan]:
        return self.repo_plan.listar_por_empresa(empresa_id)

    # ---------------------------
    # CONTRATOS
    # ---------------------------

    def contratar_plan(self, cliente_id: int, plan_id: int) -> ContratoPlan:
        """
        Un cliente contrata un plan.
        Regla: solo puede tener un contrato ACTIVO a la vez.
        """
        # Buscar contratos activos para el cliente
        contratos_cliente = self.repo_contrato.listar_por_cliente(cliente_id)

        for c in contratos_cliente:
            if c.estado == "activo":
                raise ValueError("El cliente ya tiene un contrato activo.")

        nuevo_contrato = ContratoPlan(
            id=None,
            cliente_id=cliente_id,
            plan_id=plan_id,
            fecha_inicio=date.today(),
            fecha_fin=None,
            estado="activo"
        )

        return self.repo_contrato.crear(nuevo_contrato)

    def cambiar_estado(self, contrato_id: int, nuevo_estado: str) -> ContratoPlan:
        """
        Permite suspender, reactivar o finalizar contratos.
        """
        contrato = self.repo_contrato.obtener_por_id(contrato_id)
        if not contrato:
            raise ValueError("El contrato no existe.")

        contrato.estado = nuevo_estado
        return self.repo_contrato.actualizar(contrato)
