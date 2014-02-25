# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Game, Mission, Team, Member, TeamMissionRelation


class MissionInlineAdmin(admin.TabularInline):
    model = Mission


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'finish_date', 'is_active']
    inlines = [MissionInlineAdmin]


class TeamMissionRelationInlineAdmin(admin.TabularInline):
    model = TeamMissionRelation


class MemberInlineAdmin(admin.TabularInline):
    model = Member


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_paid']
    list_editable = ['is_paid']
    inlines = [MemberInlineAdmin, TeamMissionRelationInlineAdmin]


admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
