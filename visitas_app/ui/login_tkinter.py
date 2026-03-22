import tkinter as tk

from servicios.auth_servicio import AuthServicio
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter
from ui.login_tkinter import VentanaLogin


def iniciar_app():
    root = tk.Tk()
    servicio = VisitaServicio()
    AppTkinter(root, servicio)
    root.mainloop()


def main():
    auth = AuthServicio()

    login = VentanaLogin(auth, iniciar_app)
    login.mainloop()


if __name__ == "__main__":
    main()