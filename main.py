import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from columnSelector import ColumnSelector
from scanner import Scanner
from export import Export


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Escáner TPSD")
        self.root.geometry("600x450")

        # Lógica
        self.select = ColumnSelector()
        self.scan = Scanner()
        self.export = Export()

        # UI
        self.build_ui()

    # ---------------- UI ---------------- #

    def build_ui(self):
        main = tk.Frame(self.root)
        main.pack(fill="both", expand=True)

        # HEADER
        header = tk.Frame(main, bg="#1e293b", height=80)
        header.pack(fill="x")

        tk.Label(
            header,
            text="Escáner de código TPSD",
            fg="white",
            bg="#1e293b",
            font=("Arial", 16, "bold"),
        ).pack(pady=20)

        # ESTADO
        status_frame = tk.LabelFrame(main, text="Estado")
        status_frame.pack(fill="x", padx=10, pady=5)

        self.column_label = tk.Label(
            status_frame,
            text=f"Columna activa: {self.select.get_active_column()}",
            fg="blue",
        )
        self.column_label.pack(pady=5)

        # CAMBIO DE COLUMNA
        switch_frame = tk.LabelFrame(main, text="Cambiar columna")
        switch_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(
            switch_frame, text="Columna A", command=lambda: self.switch("A")
        ).pack(side="left", padx=5, pady=5)

        tk.Button(
            switch_frame, text="Columna B", command=lambda: self.switch("B")
        ).pack(side="left", padx=5, pady=5)

        # ENTRADA
        input_frame = tk.LabelFrame(main, text="Entrada de código")
        input_frame.pack(fill="x", padx=10, pady=5)

        self.entry = tk.Entry(input_frame)
        self.entry.pack(side="left", padx=5, pady=5, fill="x", expand=True)
        self.entry.focus()

        tk.Button(input_frame, text="Escanear", command=self.scan_code).pack(
            side="left", padx=5
        )

        # Enter para escanear
        self.entry.bind("<Return>", lambda e: self.scan_code())

        # ACCIONES
        actions_frame = tk.Frame(main)
        actions_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(actions_frame, text="Exportar", command=self.export_data).pack(
            side="left", padx=5
        )

        tk.Button(actions_frame, text="Salir", command=self.root.destroy).pack(
            side="left", padx=5
        )

        # En build_ui, donde está el frame de acciones
        self.feedback_label = tk.Label(
            actions_frame, text="", font=("Arial", 10, "bold"), width=100
        )
        self.feedback_label.pack(side="left", padx=10)

        # LOG
        log_frame = tk.LabelFrame(main, text="Registro de eventos")
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.log = tk.Listbox(log_frame)
        self.log.pack(fill="both", expand=True, padx=5, pady=5)

    # ---------------- LOG ---------------- #

    def add_log(self, message, level="INFO"):
        time = datetime.now().strftime("%H:%M:%S")
        self.log.insert(tk.END, f"[{time}] [{level}] {message}")
        self.log.yview(tk.END)

    # ---------------- LÓGICA ---------------- #

    def switch(self, col):
        self.select.switch_column(col)
        self.column_label.config(
            text=f"Columna activa: {self.select.get_active_column()}"
        )
        self.add_log(f"Cambiado a columna: {col}")

    def set_feedback(self, status, code):
        if status == "added":
            self.feedback_label.config(
                text=f"✔ Agregado: {code}", fg="white", bg="#16a34a"  # verde
            )
        else:
            self.feedback_label.config(
                text=f"✘ Duplicado: {code}", fg="white", bg="#dc2626"  # rojo
            )

    def scan_code(self):
        code = self.entry.get().strip()
        if not code:
            return

        status, scanned = self.scan.scan_codes(code, self.select.get_active_column())
        col = self.select.get_active_column()

        self.set_feedback(status, scanned)
        self.add_log(
            (
                f"Código agregado: {scanned} | Col: {col}"
                if status == "added"
                else f"Duplicado: {scanned} | Col: {col}"
            ),
            level="INFO" if status == "added" else "WARNING",
        )

        self.entry.delete(0, tk.END)

    def export_data(self):
        total = self.scan.count()

        if total == 0:
            self.add_log("No hay datos para exportar")
            return

        try:
            filepath = self.export.export_code(self.scan.get_codes())

            self.add_log(f"Exportados {total} códigos")
            self.add_log(filepath)

            # 🔴 limpieza correcta
            self.scan.clear()
            self.add_log("Datos limpiados automáticamente")

        except Exception as e:
            self.add_log(f"Error al exportar: {str(e)}", level="WARNING")


# ---------------- MAIN ---------------- #


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
