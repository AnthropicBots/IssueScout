from issuescout.scanner.intelligence.pull_request import (
    PullRequestDiscussionCollector,
)


def test_collect_combines_body_and_comments():

    collector = PullRequestDiscussionCollector()

    result = collector.collect(
        body="Backport of previous fix.",
        comments=[
            "Approved.",
            "Merged.",
        ],
    )

    assert result["matched"] is True
    assert "backport" in result["keywords"]
    assert "approved" in result["keywords"]
    assert "merged" in result["keywords"]
