import pandas as pd

def normalizar_texto(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Remueve espacios en blanco y pasa el texto a mayúsculas."""
    df[columna] = df[columna].str.strip().str.upper()
    return df