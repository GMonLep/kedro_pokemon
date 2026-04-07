"""
This is a boilerplate pipeline 'practica'
generated using Kedro 1.2.0
"""
import pandas as pd

def convertir_columnas_dinero(df: pd.DataFrame) -> pd.DataFrame:
    
    cols_money = [
        "actual_gross",
        "adjusted_gross_in_2022_dollars",
        "average_gross"
    ]

    df[cols_money] = (
        df[cols_money]
        .replace(r"[^0-9.]", "", regex=True)
        .astype(float)
    )

    return df