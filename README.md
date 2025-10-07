# Analizador de vigas simplemente apoyadas

Proyecto para calcular y visualizar el comportamiento de vigas simplemente apoyadas bajo diferentes combinaciones de carga. Incluye:

- Backend modular (cálculo simbólico/numérico con SymPy / SciPy).
- Interfaz de consola (CLI).
- Frontend web con Streamlit (recomendado para usuario final).

## Estructura principal

```
backend/
├── __init__.py
├── viga.py        # Clases Viga y jerarquía de cargas
├── calculos.py    # Funciones de cálculo simbólico y numérico
├── menus.py       # Menú CLI (legacy)
├── utils.py       # Exportación de datos y utilidades varias
frontend/
└── app.py         # Interfaz Streamlit
outputs/
├── resultados_viga.csv (ejemplo)
└── graficas/
```

## Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso rápido

### Consola / Spyder

```python
from backend.menus import iniciar_menu_cli

iniciar_menu_cli()
```

### Frontend Web (Streamlit)

```bash
streamlit run frontend/app.py
```

La aplicación permite:
- Definir propiedades (L, E, I) y unidades (m↔ft, N↔kN↔lb, etc.)
- Agregar cargas: puntual, uniforme, triangular, trapezoidal
- Ver diagramas de carga, cortante, momento y deflexión
- Exportar resultados (CSV + PNG)
- Verificar principio de superposición

## Exportaciones

- Tablas en CSV con puntos discretizados (`outputs/resultados_viga.csv`).
- Gráficas en PNG ubicadas en `outputs/graficas/`.
- Comparación simbólica vs numérica opcional disponible automáticamente en los resultados.

---

## Unidades

Internamente las ecuaciones trabajan en unidades base SI: metros (m), Newtons (N), Pascales (Pa). El frontend convierte automáticamente los valores ingresados según la unidad seleccionada. Ejemplos:

- Longitud: m ↔ ft (1 ft = 0.3048 m)
- Fuerza: N ↔ kN (1 kN = 1000 N) ↔ lb (1 lb ≈ 4.4482216153 N)
- Intensidad distribuida: N/m ↔ kN/m ↔ lb/ft
- Módulo E: Pa ↔ GPa

Los resultados exportados se generan en unidades SI para evitar ambigüedad; el frontend muestra etiquetas con la unidad seleccionada.

---

CLI y antigua interfaz Notebook han sido simplificadas/retiradas para dejar un flujo principal: Streamlit.
