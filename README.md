# TPSD Scanner

Herramienta de línea de comandos para capturar códigos de barra y exportar los resultados a Excel. Nació de una necesidad real: agilizar el registro manual de códigos en dos columnas sin depender de hojas de cálculo abiertas ni digitación manual.

---

## ¿Cómo funciona?

Al ejecutar el programa, el usuario selecciona una columna (A o B) y comienza a escanear. Cada código capturado se valida automáticamente para evitar duplicados. Cuando termina, exporta todo a un archivo `.xlsx` con nombre único para que cada sesión quede registrada por separado.

```
╔══════════════════════════════════╗
║     Escaner de codigo TPSD       ║
╚══════════════════════════════════╝
  [A] Columna A    [B] Columna B
  [x] Exportar     [q] Salir
```

---

## Comandos

| Tecla | Acción |
|-------|--------|
| `A` o `B` | Cambiar columna activa |
| `x` | Exportar a Excel y continuar |
| `q` | Salir del programa |

---

## Resultado

Cada sesión genera un archivo independiente en la misma carpeta:

```
TPSD_05_04_26.xlsx
TPSD_05_04_26_(1).xlsx   ← si ya existe uno del mismo día
```

El Excel queda organizado así:

| A | B |
|---|---|
| 00123 | 00456 |
| 00124 | 00457 |

---

## Ejecutar

**Sin instalar nada** — descarga el `.exe` y ejecútalo directo (Windows 64 bits).

**Desde el código fuente:**

```bash
pip install pandas openpyxl
python main.py
```

**Generar el ejecutable:**

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

El `.exe` queda en la carpeta `dist/`.

---

## Estructura del proyecto

El proyecto está dividido en tres clases con responsabilidades claras:

```
├── main.py             # Punto de entrada y flujo principal
├── columnSelector.py   # Maneja la columna activa
├── scanner.py          # Captura códigos y previene duplicados
└── export.py           # Genera el archivo Excel con nombre único
```

---

## Tecnologías

- Python 3.x
- pandas
- openpyxl
- PyInstaller
