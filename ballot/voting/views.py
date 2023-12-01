from django.shortcuts import render, redirect

from .models import Voter, PoliticalParty
from .utils import get_all_results, get_voting, has_voted, set_vote


def index(request):
    voting = get_voting()

    if not voting.is_closed:
        return render(request, 'index.html')

    return redirect('/resultados')


def vote(request):
    voter_dni = int(request.POST['dni'])

    if has_voted(voter_dni):
        return render(request, 'index.html', {'voter_exists': True})

    voter_model = Voter.objects.get(dni=voter_dni)
    parties = PoliticalParty.objects.all()

    return render(request, 'vote.html', dict(parties=parties, voter=voter_model))


def setvote(request):
    voter_dni = int(request.POST['dni'])
    vote = request.POST['vote']

    set_vote(vote)

    Voter.objects.filter(dni=voter_dni).update(has_voted=True)

    return redirect('/')


def results(request):
    political_parties = PoliticalParty.objects.all()
    total_results = get_all_results()
    voting = get_voting()

    return render(
        request,
        'voting_results.html',
        dict(political_parties=political_parties, total_results=total_results, voting=voting),
    )
