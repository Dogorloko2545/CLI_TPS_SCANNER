from columnSelector import ColumnSelector
from scanner import Scanner
from export import Export


# Colores
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def main():
    # Se llaman las instancias
    select = ColumnSelector()
    scan = Scanner()
    export = Export()
    print(
        """
╔══════════════════════════════════╗
║     Escaner de codigo TPSD       ║
╚══════════════════════════════════╝

  [A] Columna A    [B] Columna B
  [x] Exportar     [q] Salir

  Columna activa: A

"""
    )

    while True:
        code = input(f"\nDigite codigo [{select.get_active_column()}]: ")

        if code == "q":
            print(f"{RED}[q] Usted esta saliendo...{RESET}")
            break
        elif code == "x":
            export.export_code(scan.get_codes())
        elif code.upper() in ["A", "B"]:
            select.switch_column(code)
            print(
                f"{YELLOW}[>] Cambiando a columna [{select.get_active_column()}]{RESET}"
            )
        else:
            scan.scan_codes(code, select.get_active_column())


if __name__ == "__main__":
    main()
