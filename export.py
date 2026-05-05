from datetime import datetime
from pathlib import Path
import pandas as pd


class Export:
    def __init__(self):
        self.name = "TPSD"
        self.extension = ".xlsx"

        self.base_path = Path.home() / "tpsScanner"
        self.base_path.mkdir(parents=True, exist_ok=True)

    def genera_unique_name(self):
        creation_date = datetime.now().strftime("%d_%m_%y")

        file = self.base_path / f"{self.name}_{creation_date}{self.extension}"
        cont = 1

        while file.exists():
            file = (
                self.base_path / f"{self.name}_{creation_date}_({cont}){self.extension}"
            )
            cont += 1

        return file

    def export_code(self, code: dict):
        file = self.genera_unique_name()

        df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in code.items()]))

        df.to_excel(file, index=False, header=False)

        return f"Archivo guardado en: {file}"

        return file  # 🔴 IMPORTANTE para tu UI
