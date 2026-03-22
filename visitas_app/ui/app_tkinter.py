import tkinter as tk
from tkinter import ttk, messagebox

class AppTkinter:
    def __init__(self, root, servicio):
        self.servicio = servicio
        self.root = root
        self.root.title("Sistema de Registro de Visitantes")

        # -------- FORMULARIO --------
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Cédula").grid(row=0, column=0)
        self.entry_cedula = tk.Entry(frame_form)
        self.entry_cedula.grid(row=0, column=1)

        tk.Label(frame_form, text="Nombre").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(frame_form, text="Motivo").grid(row=2, column=0)
        self.entry_motivo = tk.Entry(frame_form)
        self.entry_motivo.grid(row=2, column=1)

        # -------- BOTONES --------
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Registrar", command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Eliminar", command=self.eliminar).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Limpiar", command=self.limpiar).grid(row=0, column=2, padx=5)

        # -------- TABLA --------
        self.tree = ttk.Treeview(root, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")
        self.tree.pack(pady=10)

    # -------- FUNCIONES --------
    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        if self.servicio.registrar(cedula, nombre, motivo):
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def eliminar(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        cedula = self.tree.item(seleccionado)["values"][0]

        if self.servicio.eliminar(cedula):
            messagebox.showinfo("Éxito", "Visitante eliminado")
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo eliminar")

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for v in self.servicio.obtener_todos():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))