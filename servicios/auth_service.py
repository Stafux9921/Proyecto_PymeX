# servicios/auth_service.py

"""
Servicio de autenticación y registro de usuarios.

Aquí se maneja:
- Registrar nuevos usuarios con contraseña hasheada
- Autenticar usuarios existentes comparando hashes
- Validar formato de contraseña
"""

import hashlib
from modelos.usuario import Usuario, RolUsuario
from repositorios.usuario_repo import UsuarioRepositorio


class AuthService:
    """
    Lógica de autenticación del sistema.
    """

    def __init__(self):
        self.repo = UsuarioRepositorio()

    # ---------------------------
    # Utilidades internas
    # ---------------------------

    def _hash_password(self, password: str) -> str:
        """
        Hashea una contraseña usando SHA256 (suficiente para proyecto académico).
        """
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def _validar_password(self, password: str) -> None:
        """
        Reglas simples de validación de contraseñas.
        """
        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")

    # ---------------------------
    # Lógica principal
    # ---------------------------

    def registrar_usuario(self, nombre_usuario: str, password: str, rol: RolUsuario) -> Usuario:
        """
        Crea un nuevo usuario:
        - valida contraseña
        - valida que no exista el usuario
        - hashea contraseña
        - lo guarda en base de datos
        """
        # Validar contraseña
        self._validar_password(password)

        # Revisar si ya existe
        existente = self.repo.obtener_por_nombre(nombre_usuario)
        if existente:
            raise ValueError("Ese nombre de usuario ya está registrado.")

        # Crear objeto Usuario
        nuevo_usuario = Usuario(
            id=None,
            nombre_usuario=nombre_usuario,
            contrasena=self._hash_password(password),
            rol=rol
        )

        # Guardar
        return self.repo.crear(nuevo_usuario)

    def autenticar(self, nombre_usuario: str, password: str) -> Usuario | None:
        """
        Valida credenciales:
        - obtiene usuario por nombre
        - compara hash
        - retorna el usuario si coincide
        """
        usuario = self.repo.obtener_por_nombre(nombre_usuario)
        if not usuario:
            return None

        if usuario.contrasena == self._hash_password(password):
            return usuario

        return None
