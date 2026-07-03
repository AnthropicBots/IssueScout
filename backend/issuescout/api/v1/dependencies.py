from __future__ import annotations

from issuescout.application.container import (
    ApplicationContainer,
    get_container,
)
from issuescout.application.repository_service import (
    ApplicationRepositoryService,
)
from issuescout.scanner.engine import ScannerEngine
from issuescout.services.issue_service import IssueService
from issuescout.services.scan_job_service import ScanJobService


def get_application_container() -> ApplicationContainer:
    """
    Return the shared application container.
    """
    return get_container()


def get_repository_service() -> ApplicationRepositoryService:
    """
    Repository application service.
    """
    return get_application_container().repository_service


def get_issue_service() -> IssueService:
    """
    Issue service.
    """
    return get_application_container().issue_service


def get_scan_job_service() -> ScanJobService:
    """
    Scan job service.
    """
    return get_application_container().scan_job_service


def get_scanner_engine() -> ScannerEngine:
    """
    Scanner engine.
    """
    return get_application_container().scanner_engine
