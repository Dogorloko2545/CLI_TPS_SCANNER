# Colores
GREEN = "\033[92m"
RESET = "\033[0m"
YELLOW = "\033[93m"


class Scanner:
    def __init__(self):
        self.code = {
            "A": [],
            "B": [],
        }  # Flujo en el que se guarda cada codigo

    def scan_codes(self, scan: str, columnActive: str):
        """Recibe codigo y le quita el ultimo numero o texte que hace parte de un consecutivo, depues se guarda en la columna selecciona por el usuario"""
        scan = scan[:-1]  # quita el ultimo digito o en este caso string
        if scan not in self.code[columnActive.upper()]:
            self.code[columnActive].append(scan)
            print(f"{GREEN}[+] Codigo agregado -> {scan}{RESET}")
        else:
            print(f"{YELLOW}[!] Ya se encuentra capturado!{RESET}")

    def get_codes(self):
        """Obtine los datos de la columna activa"""
        return self.code
