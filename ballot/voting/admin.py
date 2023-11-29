from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from .models import PoliticalParty, Voter, Vote, Voting
from .utils import get_all_results, get_voting

admin.site.register(Vote)

admin.site.site_header = 'Votacion'


@admin.register(Voting, site=admin.site)
class VotingAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('cierre/', self.cierre)]
        return my_urls + urls

    def cierre(self, request):
        voting_model = Voting.objects.get()
        voting_model.is_closed = True
        voting_model.save()
        return redirect('/admin/voting/voting')

    def changelist_view(self, request, extra_context=None):
        # Genera la votacion si no existe
        get_voting()

        parties_models = PoliticalParty.objects.all()
        voting_model = Voting.objects.get()
        total_results = get_all_results()

        return super().changelist_view(
            request,
            {'voting': voting_model, 'parties': parties_models, 'total_results': total_results},
        )


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dni', 'birth_date', 'has_voted')
    search_fields = ('first_name', 'last_name', 'dni')
    list_filter = ('has_voted',)


@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ('party_number', 'party_name', 'president', 'vice_president', 'slogan')
    search_fields = ('party_number', 'party_name')
