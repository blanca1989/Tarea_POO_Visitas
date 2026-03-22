import tkinter as tk
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter

def main():
    servicio = VisitaServicio()

    root = tk.Tk()
    AppTkinter(root, servicio)
    root.mainloop()

if __name__ == "__main__":
    main()