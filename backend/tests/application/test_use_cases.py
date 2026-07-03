from unittest.mock import AsyncMock, Mock

import pytest

from issuescout.application.use_cases.evaluate_dataset import (
    EvaluateDatasetUseCase,
)
from issuescout.application.use_cases.generate_dataset import (
    GenerateDatasetUseCase,
)
from issuescout.application.use_cases.predict_issue import (
    PredictIssueUseCase,
)
from issuescout.application.use_cases.scan_repository import (
    ScanRepositoryUseCase,
)


def test_evaluate_dataset_use_case():
    service = Mock()

    service.evaluate_dataset.return_value = "summary"

    use_case = EvaluateDatasetUseCase(
        service,
    )

    result = use_case.execute(
        "dataset.json",
    )

    assert result == "summary"

    service.evaluate_dataset.assert_called_once_with(
        "dataset.json",
    )


@pytest.mark.anyio
async def test_generate_dataset_use_case():
    generator = AsyncMock()

    generator.generate.return_value = "dataset"

    use_case = GenerateDatasetUseCase(
        generator,
    )

    result = await use_case.execute(
        "owner",
        "repo",
        limit=25,
    )

    assert result == "dataset"

    generator.generate.assert_awaited_once_with(
        "owner",
        "repo",
        limit=25,
    )

    await use_case.close()

    generator.close.assert_awaited_once()


@pytest.mark.anyio
async def test_predict_issue_use_case():
    service = AsyncMock()

    service.predict.return_value = "prediction"

    use_case = PredictIssueUseCase(
        service,
    )

    issue = object()
    prs = [object()]

    result = await use_case.execute(
        issue,
        prs,
        verbose=True,
    )

    assert result == "prediction"

    service.predict.assert_awaited_once_with(
        issue,
        prs,
        verbose=True,
    )


@pytest.mark.anyio
async def test_scan_repository_use_case():
    service = AsyncMock()

    service.scan_repository.return_value = "scan"

    use_case = ScanRepositoryUseCase(
        service,
    )

    result = await use_case.execute(
        "owner",
        "repo",
    )

    assert result == "scan"

    service.scan_repository.assert_awaited_once_with(
        "owner",
        "repo",
    )
