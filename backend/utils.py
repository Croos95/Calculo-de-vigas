"""Utilidades para exportación de resultados y manejo de rutas."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from .units import LENGTH_UNITS, FORCE_UNITS, DEFLEXION_DISPLAY  # nuevos imports

OUTPUT_DIR = Path("outputs")
GRAFICAS_DIR = OUTPUT_DIR / "graficas"


def asegurar_directorios() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    GRAFICAS_DIR.mkdir(exist_ok=True, parents=True)


def exportar_tabla(dataframe: pd.DataFrame, nombre: str) -> Path:
    asegurar_directorios()
    ruta = OUTPUT_DIR / f"{nombre}.csv"
    dataframe.to_csv(ruta, index=False)
    return ruta


def exportar_grafica(figura, nombre: str) -> Path:
    asegurar_directorios()
    ruta = GRAFICAS_DIR / f"{nombre}.png"
    figura.savefig(ruta, dpi=200, bbox_inches="tight")
    return ruta


def formatear_maximos(maximos: dict) -> str:
    lineas = []
    for clave, (posicion, valor) in maximos.items():
        lineas.append(
            f"{clave.capitalize()}: {valor: .4e} en x = {posicion: .3f} m"
        )
    return "\n".join(lineas)


def convertir_dataframe_export(
    df_si: pd.DataFrame, len_unit: str, force_unit: str, defl_unit: str
) -> pd.DataFrame:
    """Convierte un DataFrame en SI a unidades solicitadas (solo columnas conocidas).

    Parámetros
    ---------
    df_si: DataFrame con columnas en SI (x, cortante [N], momento [N*m], deflexion [m])
    len_unit, force_unit, defl_unit: nombres de unidades destino.

    Retorna
    -------
    DataFrame convertido (copia) listo para exportar.
    """
    df = df_si.copy()
    fL = LENGTH_UNITS[len_unit]
    fF = FORCE_UNITS[force_unit]
    fDef = DEFLEXION_DISPLAY[defl_unit]
    if "x" in df:
        df["x"] = df["x"] / fL
    if "cortante" in df:
        df["cortante"] = df["cortante"] / fF
    if "momento" in df:
        df["momento"] = df["momento"] / (fF * fL)
    if "deflexion" in df:
        df["deflexion"] = df["deflexion"] / fDef
    return df
