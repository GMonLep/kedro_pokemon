"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines.practica import create_pipeline as practica_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines(raise_errors=True)
    pipelines["practica"] = practica_pipeline()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
