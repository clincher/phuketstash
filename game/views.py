# -*- coding: utf-8 -*-
from datetime import date

from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from django.views.generic import CreateView, DetailView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404

from models import Game, Team, Member


class TeamDetailView(DetailView):
    model = Team


class TeamRequestView(CreateView):
    model = Team
    fields = ['name']

    def get(self, request, *args, **kwargs):
        if request.game.team_set.filter(owner=request.user).exists():
            self.object = request.game.team_set.filter(owner=request.user)[0]
            return HttpResponseRedirect(self.get_success_url())
        super(TeamRequestView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.game:
            self.object.game = self.request.game
        else:
            form.errors.append(u'there is no active games in that moment')
            return self.form_invalid(form)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class MemberJoinView(DetailView):
    model = Team

    def get(self, request, *args, **kwargs):
        team = self.get_object()
        Member.objects.filter(team__game=team.game, user=request.user).delete()
        Member.objects.create(team=team, user=request.user)
        return HttpResponseRedirect(
            reverse('team-detail', kwargs={'pk': team.pk}))
