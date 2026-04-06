from datetime import datetime
from pathlib import Path
import pandas as pd

# Colores
GREEN = "\033[92m"
RESET = "\033[0m"


class Export:
    def __init__(self):
        self.name = "TPSD"
        self.creation_date = datetime.now().strftime("%d_%m_%y")
        self.base_path = Path(__file__).parent
        self.extension = ".xlsx"
        self.file_name = (
            self.base_path / f"{self.name}_{self.creation_date}{self.extension}"
        )

    def genera_unique_name(self):
        """Genera nombre unico de archivo excel"""
        file = self.file_name
        cont = 1
        while file.exists():
            file = (
                self.base_path
                / f"{self.name}_{self.creation_date}_({cont}){self.extension}"
            )
            cont += 1

        self.file_name = file
        return self.file_name

    def export_code(self, code: dict):
        """Exportaa en un archivo excel los datos o codigo"""
        file = self.genera_unique_name()  # genera nombre de archivo unico
        df = pd.DataFrame(
            dict([(k, pd.Series(v)) for k, v in code.items()])
        )  # pasa la funcion y la convierte en columna
        df.to_excel(file, index=False, header=False)
        print(f"{GREEN}[x] Archivo guardado en: {file} {RESET}")
