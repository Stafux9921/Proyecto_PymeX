# main.py

"""
Punto de entrada del programa ISPPlus.

Por ahora implementa un menú de consola muy simple que permite:
- Inicializar la base de datos.
- Registrar usuarios.
- Iniciar sesión.

Más adelante puedes extender este menú para:
- Gestionar empresas, clientes, planes y contratos.
- Consultar indicadores económicos a través de la API externa.
"""

from getpass import getpass  # para escribir contraseñas sin mostrarlas
from db.init_db import init_db
from servicios.auth_service import AuthService
from modelos.usuario import RolUsuario
from config import APP_NAME


def mostrar_banner():
    print("=" * 50)
    print(f"{APP_NAME} - Backend (modo consola)")
    print("=" * 50)


def menu_principal() -> str:
    print("\nMenú principal")
    print("1) Registrar nuevo usuario")
    print("2) Iniciar sesión")
    print("0) Salir")
    return input("Elija una opción: ").strip()


def menu_usuario_autenticado(usuario):
    """
    Menú de ejemplo para cuando un usuario ya inició sesión.
    Aquí más adelante puedes ramificar según rol:
    - cliente: ver su plan, contratar, etc.
    - empresa: gestionar sus planes.
    - admin: ver todo.
    """
    print(f"\nBienvenido, {usuario.nombre_usuario} (rol: {usuario.rol})")
    print("Este es un menú de ejemplo para usuario autenticado.")
    print("Aquí luego podrás:")
    print("- Gestionar planes")
    print("- Ver/crear contratos")
    print("- Consultar indicadores económicos")
    input("Presione ENTER para volver al menú principal...")


def registrar_usuario(auth_service: AuthService):
    """
    Flujo para registrar un nuevo usuario desde consola.
    """
    print("\n=== Registrar nuevo usuario ===")
    nombre_usuario = input("Nombre de usuario: ").strip()
    password = getpass("Contraseña: ")
    password2 = getpass("Repita la contraseña: ")

    if password != password2:
        print("❌ Las contraseñas no coinciden.")
        return

    print("Roles disponibles: cliente / empresa / admin")
    rol_str = input("Rol: ").strip().lower()

    try:
        rol = RolUsuario(rol_str)
    except ValueError:
        print("❌ Rol inválido.")
        return

    try:
        usuario = auth_service.registrar_usuario(nombre_usuario, password, rol)
        print(f"✅ Usuario creado con id {usuario.id}")
    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")


def iniciar_sesion(auth_service: AuthService):
    """
    Flujo de login desde consola.
    """
    print("\n=== Iniciar sesión ===")
    nombre_usuario = input("Nombre de usuario: ").strip()
    password = getpass("Contraseña: ")

    usuario = auth_service.autenticar(nombre_usuario, password)
    if not usuario:
        print("❌ Credenciales incorrectas.")
        return

    # Si quieres, aquí podrías guardar el usuario en una variable global
    # o pasarlo a otros menús según su rol.
    menu_usuario_autenticado(usuario)


def main():
    """
    Función principal del programa.
    """
    mostrar_banner()

    # 1. Inicializar la base de datos (crear tablas si no existen)
    init_db()

    # 2. Crear instancia del servicio de autenticación
    auth_service = AuthService()

    # 3. Bucle principal
    while True:
        opcion = menu_principal()

        if opcion == "1":
            registrar_usuario(auth_service)
        elif opcion == "2":
            iniciar_sesion(auth_service)
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
