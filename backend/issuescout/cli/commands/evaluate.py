from __future__ import annotations

from issuescout.evaluation.runner import EvaluationRunner


def evaluate() -> EvaluationRunner:
    """
    Create an evaluation runner.

    Future CLI arguments will configure the runner.
    """

    return EvaluationRunner()
