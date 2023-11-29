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
    return Voting.objects.get_or_create()[0]


def set_vote(vote):
    if vote.isdigit():
        party_model = vote
    else:
        party_model = False

    if vote == 'white':
        vote_white = True
    else:
        vote_white = False

    if vote == 'null':
        vote_null = True
    else:
        vote_null = False

    vote_model = Vote(party_number=party_model, white=vote_white, null=vote_null)

    vote_model.save()

    return vote_model


def get_party_percentage(party):
    total_votes = Vote.objects.all().count()
    party_votes = Vote.objects.filter(party_number=party.party_number).count()

    if party_votes == 0:
        return 0

    return round((party_votes / total_votes) * 100, 2)


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
    voting_model = Voting.objects.get()
    vote_models = Vote.objects.all()
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
