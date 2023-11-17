import pytest

from voting.utils import has_voted, has_voted_percentage
from .factories import VoterFactory


@pytest.mark.django_db
def test_has_voted_true():
    voter = VoterFactory(has_voted=True)

    assert has_voted(voter.dni) is True


@pytest.mark.django_db
def test_has_voted_false():
    voter = VoterFactory(has_voted=False)

    assert has_voted(voter.dni) is False


@pytest.mark.django_db
def test_has_voted_not_exits():
    assert has_voted(1234) is None


@pytest.mark.django_db
def test_has_voted_percentage_when_0_voters():
    voted_percentage = has_voted_percentage()

    assert voted_percentage == pytest.approx(0, abs=0.01)


@pytest.mark.django_db
def test_has_voted_percentage_when_all_voters_voted():
    VoterFactory(has_voted=True, dni=1)
    VoterFactory(has_voted=True, dni=2)
    VoterFactory(has_voted=True, dni=3)
    VoterFactory(has_voted=True, dni=4)

    voted_percentage = has_voted_percentage()

    assert voted_percentage == pytest.approx(100, abs=0.01)


@pytest.mark.django_db
def test_has_voted_percentage_when_50_50():
    VoterFactory(has_voted=True, dni=1)
    VoterFactory(has_voted=True, dni=2)
    VoterFactory(has_voted=False, dni=3)
    VoterFactory(has_voted=False, dni=4)

    voted_percentage = has_voted_percentage()

    assert voted_percentage == pytest.approx(50, abs=0.01)
