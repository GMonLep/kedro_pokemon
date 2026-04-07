"""
This is a boilerplate pipeline 'practica'
generated using Kedro 1.2.0
"""

from kedro.pipeline import Node, Pipeline  # noqa
from .nodes import convertir_columnas_dinero

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=convertir_columnas_dinero,
            inputs="datos_practica",
            outputs="datos_practica_listo",
            name="convert_money_columns_node",
        )
    ])
