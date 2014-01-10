# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import izip

from pytz import common_timezones
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from utils.annoying import nullable
from managers import EmailUserManager


class Referer(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'{0}'.format(self.name)


class User(AbstractBaseUser, PermissionsMixin):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский')
    )

    TIMEZONE_CHOICES = izip(common_timezones, common_timezones)

    email = models.EmailField(
        _('Электронная почта'), max_length=255, unique=True, db_index=True)
    first_name = models.CharField(_('Имя'), max_length=30, **nullable)
    last_name = models.CharField(_('Фамилия'), max_length=30, **nullable)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active = models.BooleanField(
        _('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    # Info fields
    url = models.URLField('Профиль в вк/фб', **nullable)
    gender = models.IntegerField('Пол', choices=GENDER_CHOICES, **nullable)
    birth_date = models.DateField('Дата рождения', **nullable)
    phone_number = models.CharField('Номер телефона', max_length=22, **nullable)
    is_available = models.BooleanField(default=True)
    arrive_date = models.DateTimeField(**nullable)
    timezone = models.CharField(
        'Часовой пояс', max_length=30, choices=TIMEZONE_CHOICES,
        default='Asia/Bangkok')
    bio = models.TextField(
        _('О себе'), help_text=_('Расскажите немного о себе'), **nullable)
    userpic_origin = models.ImageField('Аватар', upload_to='userpic',
                                help_text=_('Выберите изображение'), **nullable)
    comment = models.TextField('Комментарий', **nullable)

    referer = models.ForeignKey(Referer, **nullable)
    need_sleeping = models.BooleanField(default=True)
    pastimes = models.ManyToManyField('pastimes.Pastime',
                                       related_name='users', **nullable)

    objects = EmailUserManager()

    EMAIL_FIELD = USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('user-detail', args=(self.pk,))

    def get_full_name(self):
        return ' '.join(filter(bool, (
            self.first_name, self.last_name))) or self.email

    def get_short_name(self):
        return '' # TODO NotImplementedError
