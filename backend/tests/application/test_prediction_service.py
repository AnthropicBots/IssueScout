from unittest.mock import AsyncMock

import pytest

from issuescout.application.prediction_service import (
    ApplicationPredictionService,
)


@pytest.mark.anyio
async def test_predict():
    prediction = AsyncMock()

    prediction.predict.return_value = "prediction"

    service = ApplicationPredictionService(
        prediction,
    )

    issue = object()
    prs = [object()]

    result = await service.predict(
        issue,
        prs,
        verbose=True,
    )

    assert result == "prediction"

    prediction.predict.assert_awaited_once_with(
        issue,
        prs,
        verbose=True,
    )
