# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from utils.annoying import nullable


class Game(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(**nullable)
    start_date = models.DateField()
    finish_date = models.DateField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Игра'
        verbose_name_plural = u'Игры'

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Mission(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=70)
    desc = models.TextField(**nullable)
    hint = models.TextField(**nullable)
    hint2 = models.TextField(**nullable)
    image = models.ImageField(upload_to='missions', **nullable)

    class Meta:
        verbose_name = u'Задание'
        verbose_name_plural = u'Задания'

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Team(models.Model):
    name = models.CharField(max_length=70, verbose_name=u'Team name')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_paid = models.BooleanField(default=False)
    game = models.ForeignKey(Game)

    class Meta:
        verbose_name = u'Команда'
        verbose_name_plural = u'Команды'

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def get_absolute_url(self):
        return reverse('team-detail', kwargs={'pk': self.pk})


class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    team = models.ForeignKey(Team, verbose_name=u'Team')

    class Meta:
        verbose_name = u'Участник'
        verbose_name_plural = u'Участники'

    def __unicode__(self):
        return u'{0}'.format(self.user)


class TeamMissionRelation(models.Model):
    team = models.ForeignKey(Team)
    mission = models.ForeignKey(Mission)
    points = models.IntegerField(**nullable)

    class Meta:
        verbose_name = u'Взаимосвязь команда-задание'
        verbose_name_plural = u'Взаимосвязи команд и заданий'

    def __unicode__(self):
        return u'{0} - {1}'.format(self.team.name, self.mission.name)
