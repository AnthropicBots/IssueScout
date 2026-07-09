import pytest

from issuescout.scanner.intelligence.issue.enricher import (
    IssueEnricher,
)

from tests.helpers.factories import make_issue


@pytest.mark.anyio
async def test_enrich_returns_same_issue():
    issue = make_issue()

    enricher = IssueEnricher()

    enriched = await enricher.enrich(issue)

    assert enriched is issue
