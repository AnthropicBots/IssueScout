from issuescout.models import (
    Issue,
    PullRequest,
)
from issuescout.scanner.evidence.collector import (
    RelationshipEvidenceCollector,
)


def test_collect_relationship_evidence():

    collector = RelationshipEvidenceCollector()

    issue = Issue(
        number=1,
        title="Issue",
        author="alice",
        body_pull_requests={10},
        comment_pull_requests={10},
        timeline_pull_requests=set(),
        commit_pull_requests={20},
    )

    pull_request = PullRequest(
        number=10,
        title="PR",
        body="",
        author="alice",
        branch_name="main",
    )

    evidence = collector.collect(
        issue,
        pull_request,
    )

    assert evidence["body_reference"] is True
    assert evidence["comment_reference"] is True
    assert evidence["timeline_reference"] is False
    assert evidence["commit_reference"] is False
    assert evidence["reference_count"] == 2


def test_collect_relationship_evidence_without_matches():

    collector = RelationshipEvidenceCollector()

    issue = Issue(
        number=1,
        title="Issue",
        author="alice",
    )

    pull_request = PullRequest(
        number=99,
        title="PR",
        body="",
        author="alice",
        branch_name="main",
    )

    evidence = collector.collect(
        issue,
        pull_request,
    )

    assert evidence["reference_count"] == 0
