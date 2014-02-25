# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from views import TeamRequestView, MemberJoinView, TeamDetailView

urlpatterns = [
    url(r'^team-request/$',
        login_required(TeamRequestView.as_view()),
        name='team-request'
    ),
    url(r'^team/(?P<pk>\d+)/$',
        login_required(TeamDetailView.as_view()),
        name='team-detail'
    ),
    url(r'^join-team/(?P<pk>\d+)/$',
        login_required(MemberJoinView.as_view()),
        name='team-join'
    ),
    #url(r'^member-request/$',
    #    login_required(MemberRequestView.as_view()),
    #    name='member-request'
    #),
]
