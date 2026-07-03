from issuescout.application.container import (
    get_container,
)
from issuescout.application.evaluation_service import (
    ApplicationEvaluationService,
)
from issuescout.application.prediction_service import (
    ApplicationPredictionService,
)
from issuescout.application.repository_service import (
    ApplicationRepositoryService,
)
from issuescout.application.scan_service import (
    ApplicationScanService,
)
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


def test_container_is_singleton():
    first = get_container()
    second = get_container()

    assert first is second


def test_application_services_exist():
    container = get_container()

    assert isinstance(
        container.repository,
        ApplicationRepositoryService,
    )

    assert isinstance(
        container.scanner,
        ApplicationScanService,
    )

    assert isinstance(
        container.prediction,
        ApplicationPredictionService,
    )

    assert isinstance(
        container.evaluation,
        ApplicationEvaluationService,
    )


def test_use_cases_exist():
    container = get_container()

    assert isinstance(
        container.scan_repository_use_case,
        ScanRepositoryUseCase,
    )

    assert isinstance(
        container.predict_issue_use_case,
        PredictIssueUseCase,
    )

    assert isinstance(
        container.generate_dataset_use_case,
        GenerateDatasetUseCase,
    )

    assert isinstance(
        container.evaluate_dataset_use_case,
        EvaluateDatasetUseCase,
    )
