from issuescout.ranking import Ranker


def test_ranker_empty():
    ranker = Ranker()

    assert ranker.rank([]) == []
