class AuthServicio:

    def __init__(self):
        self._usuarios = {
            "admin": "1567",
            "maria": "3456"
        }

    def validar_credenciales(self, usuario: str, password: str) -> bool:
        return self._usuarios.get(usuario) == password