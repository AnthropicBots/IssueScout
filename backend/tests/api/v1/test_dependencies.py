from unittest.mock import Mock, patch

from issuescout.api.v1.dependencies import (
    get_application_container,
    get_issue_service,
    get_repository_service,
    get_scan_job_service,
    get_scanner_engine,
)


def test_get_application_container():

    container = Mock()

    with patch(
        "issuescout.api.v1.dependencies.get_container",
        return_value=container,
    ):
        assert get_application_container() is container


def test_get_repository_service():

    repository_service = Mock()

    container = Mock()
    container.repository_service = repository_service

    with patch(
        "issuescout.api.v1.dependencies.get_application_container",
        return_value=container,
    ):
        assert get_repository_service() is repository_service


def test_get_issue_service():

    issue_service = Mock()

    container = Mock()
    container.issue_service = issue_service

    with patch(
        "issuescout.api.v1.dependencies.get_application_container",
        return_value=container,
    ):
        assert get_issue_service() is issue_service


def test_get_scan_job_service():

    scan_job_service = Mock()

    container = Mock()
    container.scan_job_service = scan_job_service

    with patch(
        "issuescout.api.v1.dependencies.get_application_container",
        return_value=container,
    ):
        assert get_scan_job_service() is scan_job_service


def test_get_scanner_engine():

    scanner_engine = Mock()

    container = Mock()
    container.scanner_engine = scanner_engine

    with patch(
        "issuescout.api.v1.dependencies.get_application_container",
        return_value=container,
    ):
        assert get_scanner_engine() is scanner_engine
