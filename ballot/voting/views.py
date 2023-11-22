from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Voter, Vote, PoliticalParty, Voting
from .utils import has_voted, has_voted_percentage, get_voting, set_vote, get_all_results
import datetime

def index(request):
    voting = get_voting()
    if not voting.is_closed:
        return render(request, "index.html")
    else:
        return redirect("/resultados")

def vote(request):
    voter_dni = int(request.POST['dni'])
    if has_voted(voter_dni):
        return render(request, "index.html", {
            "voter_exists": True
        })
    voter_model = Voter.objects.get(dni=voter_dni)
    parties = PoliticalParty.objects.all()
    return render(request, "vote.html", {"parties": parties, "voter": voter_model})

def setvote(request):
    vote_model = set_vote(request.POST['vote'])
    voter_model = Voter.objects.get(dni=request.POST['dni'])
    voter_model.has_voted = True
    voter_model.save()
    return redirect("/")

def results(request):
    political_parties = PoliticalParty.objects.all()
    total_results = get_all_results()
    voting = get_voting()

    return render(
        request, 
        "voting_results.html", 
        {
            "political_parties": political_parties,
            "total_results": total_results,
            "voting": voting
        }
    )
