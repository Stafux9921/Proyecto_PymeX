# repositorios/usuario_repo.py

from modelos.usuario import Usuario, RolUsuario
from repositorios.base import BaseRepositorio
from db.connection import db


class UsuarioRepositorio(BaseRepositorio[Usuario]):

    # ==========================================================================
    # Métodos requeridos por BaseRepositorio (del profe)
    # ==========================================================================

    def agregar(self, usuario: Usuario) -> Usuario:
        """
        Método exigido por BaseRepositorio.
        Delegamos al método 'crear', que es el real en este proyecto.
        """
        return self.crear(usuario)

    def listar_todos(self) -> list[Usuario]:
        """
        Método exigido por BaseRepositorio.
        Delegamos al método 'listar', que es el real en este proyecto.
        """
        return self.listar()

    # ==========================================================================
    # Métodos reales que usa el proyecto ISPPlus
    # ==========================================================================

    def crear(self, usuario: Usuario) -> Usuario:
        with db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO usuarios (nombre_usuario, contrasena, rol)
                VALUES (?, ?, ?)
                """,
                (usuario.nombre_usuario, usuario.contrasena, usuario.rol.value)
            )
            usuario.id = cur.lastrowid
        return usuario

    def obtener_por_id(self, usuario_id: int) -> Usuario | None:
        with db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT id, nombre_usuario, contrasena, rol
                FROM usuarios
                WHERE id = ?
                """,
                (usuario_id,)
            )
            fila = cur.fetchone()

        return self._fila_a_usuario(fila) if fila else None

    def obtener_por_nombre(self, nombre_usuario: str) -> Usuario | None:
        with db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT id, nombre_usuario, contrasena, rol
                FROM usuarios
                WHERE nombre_usuario = ?
                """,
                (nombre_usuario,)
            )
            fila = cur.fetchone()

        return self._fila_a_usuario(fila) if fila else None

    def listar(self) -> list[Usuario]:
        with db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT id, nombre_usuario, contrasena, rol
                FROM usuarios
                """
            )
            filas = cur.fetchall()

        return [self._fila_a_usuario(f) for f in filas]

    def actualizar(self, usuario: Usuario) -> Usuario:
        with db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE usuarios
                SET nombre_usuario = ?, contrasena = ?, rol = ?
                WHERE id = ?
                """,
                (usuario.nombre_usuario, usuario.contrasena, usuario.rol.value, usuario.id)
            )
        return usuario

    def eliminar(self, usuario_id: int) -> None:
        with db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM usuarios WHERE id = ?", (usuario_id,)
            )

    # ==========================================================================
    # Helper interno
    # ==========================================================================

    def _fila_a_usuario(self, fila) -> Usuario:
        return Usuario(
            id=fila[0],
            nombre_usuario=fila[1],
            contrasena=fila[2],
            rol=RolUsuario(fila[3])
        )
