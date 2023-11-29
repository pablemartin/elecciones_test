from .models import Voter, Voting, PoliticalParty, Vote


def has_voted(dni):
    try:
        voter = Voter.objects.get(dni=dni)
        return voter.has_voted
    except Voter.DoesNotExist:
        return None


def has_voted_percentage():
    total_voters = Voter.objects.count()
    voted_voters = Voter.objects.filter(has_voted=True).count()

    if total_voters == 0:
        return 0

    return round((voted_voters / total_voters) * 100, 2)


def get_voting():
    voting, _ = Voting.objects.get_or_create()

    return voting


def set_vote(vote):
    political_party = None
    if vote.isdigit():
        party_number = vote
        political_party = PoliticalParty.objects.get(party_number=party_number)

    vote_white = vote == 'white'
    vote_null = vote == 'null'
    vote_model = Vote.objects.create(
        political_party=political_party, white=vote_white, null=vote_null
    )

    return vote_model


def get_party_percentage(party):
    total_party_votes = Vote.objects.filter(political_party__isnull=False).count()
    party_votes = Vote.objects.filter(political_party=party).count()

    if total_party_votes == 0:
        return 0

    return round((party_votes / total_party_votes) * 100, 2)


def get_white_percentage():
    total_votes = Vote.objects.all().count()
    white_votes = Vote.objects.filter(white=True).count()
    if white_votes == 0:
        return 0
    return round((white_votes / total_votes) * 100, 2)


def get_null_percentage():
    total_votes = Vote.objects.all().count()
    null_votes = Vote.objects.filter(null=True).count()

    if null_votes == 0:
        return 0

    return round((null_votes / total_votes) * 100, 2)


def get_all_results():
    parties_models = PoliticalParty.objects.all()
    white_percentage = get_white_percentage()
    null_percentage = get_null_percentage()
    voted_percentage = has_voted_percentage()
    total_voters = Voter.objects.count()
    parties_results = {}
    winner_percentage = 0
    winner_party = False

    for party in parties_models:
        percentage = get_party_percentage(party)
        parties_results.update({party.party_name: percentage})
        if percentage > winner_percentage:
            winner_percentage = percentage
            winner_party = party.party_name

    return {
        'parties_results': parties_results,
        'whites': white_percentage,
        'nulls': null_percentage,
        'voted_percentage': voted_percentage,
        'total_voters': total_voters,
        'winner': winner_party,
    }
