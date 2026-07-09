from issuescout.scanner.intelligence.issue.timeline_reference_collector import (
    IssueTimelineReferenceCollector,
)

from tests.helpers.factories import make_issue


def test_collect_timeline_reference():
    issue = make_issue()

    collector = IssueTimelineReferenceCollector()

    collector.collect(
        issue,
        [
            {
                "source": {
                    "issue": {
                        "body": "Backport of #33",
                    }
                }
            }
        ],
    )

    assert issue.timeline_pull_requests == {33}


def test_collect_invalid_event():
    issue = make_issue()

    collector = IssueTimelineReferenceCollector()

    collector.collect(
        issue,
        [
            {},
            {"source": None},
            {"source": {}},
        ],
    )

    assert issue.timeline_pull_requests == set()
