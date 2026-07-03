from __future__ import annotations

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
from issuescout.evaluation.loader import EvaluationLoader
from issuescout.evaluation.pipeline import EvaluationPipeline
from issuescout.evaluation.runner import EvaluationRunner
from issuescout.prediction.prediction_service import PredictionService
from issuescout.scanner.engine import ScannerEngine
from issuescout.scanner.relation import RelationEngine
from issuescout.scanner.relation.registry import (
    default_analyzers,
)
from issuescout.services.issue_service import IssueService
from issuescout.services.repository_service import RepositoryService
from issuescout.services.scan_job_service import ScanJobService
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


class ApplicationContainer:
    """
    Central dependency container for the IssueScout application.

    The container owns shared infrastructure objects and exposes
    high-level application services to the API, CLI, and future UI.
    """

    def __init__(self) -> None:
        #
        # Shared infrastructure
        #
        self._relation_engine = RelationEngine(
            default_analyzers(),
        )

        self._scanner_engine = ScannerEngine()

        self._repository_service = RepositoryService()

        self._issue_service = IssueService()

        self._scan_job_service = ScanJobService(
            scanner_engine=self._scanner_engine,
        )

        self._prediction_engine = PredictionService(
            relation_engine=self._relation_engine,
        )

        self._evaluation_runner = EvaluationRunner()

        self._evaluation_loader = EvaluationLoader()

        self._evaluation_pipeline = EvaluationPipeline()

        self._repository = ApplicationRepositoryService(
            self._repository_service,
        )

        self._scanner = ApplicationScanService(
            self._scanner_engine,
        )

        self._prediction = ApplicationPredictionService(
            self._prediction_engine,
        )

        self._evaluation = ApplicationEvaluationService(
            runner=self._evaluation_runner,
            loader=self._evaluation_loader,
            pipeline=self._evaluation_pipeline,
        )

        #
        # Use cases
        #

        self._scan_repository = ScanRepositoryUseCase(
            self._scanner,
        )

        self._predict_issue = PredictIssueUseCase(
            self._prediction,
        )

        self._generate_dataset = GenerateDatasetUseCase()

        self._evaluate_dataset = EvaluateDatasetUseCase(
            self._evaluation,
        )

    @property
    def repository(
        self,
    ) -> ApplicationRepositoryService:
        return self._repository

    @property
    def scanner(
        self,
    ) -> ApplicationScanService:
        return self._scanner

    @property
    def prediction(
        self,
    ) -> ApplicationPredictionService:
        return self._prediction

    @property
    def repository_service(
        self,
    ) -> ApplicationRepositoryService:
        return self._repository

    @property
    def issue_service(
        self,
    ) -> IssueService:
        return self._issue_service

    @property
    def scan_job_service(
        self,
    ) -> ScanJobService:
        return self._scan_job_service

    @property
    def scanner_engine(
        self,
    ) -> ScannerEngine:
        return self._scanner_engine

    @property
    def evaluation(
        self,
    ) -> ApplicationEvaluationService:
        return self._evaluation

    @property
    def scan_repository_use_case(
        self,
    ) -> ScanRepositoryUseCase:
        return self._scan_repository

    @property
    def predict_issue_use_case(
        self,
    ) -> PredictIssueUseCase:
        return self._predict_issue

    @property
    def generate_dataset_use_case(
        self,
    ) -> GenerateDatasetUseCase:
        return self._generate_dataset

    @property
    def evaluate_dataset_use_case(
        self,
    ) -> EvaluateDatasetUseCase:
        return self._evaluate_dataset


_container: ApplicationContainer | None = None


def get_container() -> ApplicationContainer:
    """
    Return the shared application container.

    The container is created lazily so that expensive
    infrastructure is only initialized when first needed.
    """
    global _container

    if _container is None:
        _container = ApplicationContainer()

    return _container
