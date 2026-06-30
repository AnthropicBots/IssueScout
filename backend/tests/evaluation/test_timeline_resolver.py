from issuescout.evaluation.resolvers.timeline import TimelineRelationResolver


def test_resolve_empty_timeline():
    resolver = TimelineRelationResolver()

    relation = resolver.resolve([])

    assert relation.pull_request_number is None
    assert relation.resolved is False
    assert relation.confidence == 0.0


def test_resolve_cross_referenced_event():
    resolver = TimelineRelationResolver()

    timeline = [
        {
            "event": "cross-referenced",
            "source": {
                "issue": {
                    "number": 152534,
                    "pull_request": {},
                },
            },
        },
    ]

    relation = resolver.resolve(timeline)

    assert relation.resolved is True
    assert relation.pull_request_number == 152534
    assert relation.confidence == 1.0
    assert relation.linkage_method == "cross-referenced"


def test_ignore_non_pr_cross_reference():
    resolver = TimelineRelationResolver()

    timeline = [
        {
            "event": "cross-referenced",
            "source": {
                "issue": {
                    "number": 12345,
                },
            },
        },
    ]

    relation = resolver.resolve(timeline)

    assert relation.resolved is False


def test_ignore_unknown_events():
    resolver = TimelineRelationResolver()

    timeline = [
        {
            "event": "assigned",
        },
        {
            "event": "labeled",
        },
        {
            "event": "milestoned",
        },
    ]

    relation = resolver.resolve(timeline)

    assert relation.resolved is False


def test_first_valid_pr_is_selected():
    resolver = TimelineRelationResolver()

    timeline = [
        {
            "event": "cross-referenced",
            "source": {
                "issue": {
                    "number": 100,
                    "pull_request": {},
                },
            },
        },
        {
            "event": "cross-referenced",
            "source": {
                "issue": {
                    "number": 200,
                    "pull_request": {},
                },
            },
        },
    ]

    relation = resolver.resolve(timeline)

    assert relation.pull_request_number == 100
    assert len(relation.evidence) == 2


def test_closed_event_marks_issue_closed():
    resolver = TimelineRelationResolver()

    timeline = [
        {
            "event": "closed",
        },
    ]

    relation = resolver.resolve(timeline)

    assert relation.closed_issue is True
    assert relation.resolved is False


def test_referenced_event_without_pr_does_not_resolve():
    resolver = TimelineRelationResolver()

    timeline = [
        {
            "event": "referenced",
        },
    ]

    relation = resolver.resolve(timeline)

    assert relation.resolved is False


def test_highest_confidence_candidate_is_selected():
    resolver = TimelineRelationResolver()

    timeline = [
        {
            "event": "cross-referenced",
            "source": {
                "issue": {
                    "number": 100,
                    "pull_request": {},
                },
            },
        },
        {
            "event": "cross-referenced",
            "source": {
                "issue": {
                    "number": 200,
                    "pull_request": {},
                },
            },
        },
    ]

    relation = resolver.resolve(timeline)

    assert relation.pull_request_number == 100
