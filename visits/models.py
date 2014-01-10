# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from utils.annoying import nullable


class Plan(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    price = models.IntegerField('Цена')
    visits = models.IntegerField('Количество визитов')
    days = models.IntegerField()
    daily_fees = models.BooleanField(default=False)
    comment = models.TextField(**nullable)

    class Meta:
        verbose_name = u'Тарифный план'
        verbose_name_plural = u'Тарифные планы'

    def __unicode__(self):
        return u'{0} - {1}THB'.format(self.name, self.price)


class Subscription(models.Model):
    administrant = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='subscribers')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='subscriptions')
    plan = models.ForeignKey(Plan, limit_choices_to={'is_active': True})
    start_date = models.DateTimeField(default=datetime.now())
    expire_date = models.DateTimeField(**nullable)

    class Meta:
        verbose_name = u'Подписка'
        verbose_name_plural = u'Подписки'

    def __unicode__(self):
        return u'{0}: {1} - {2}'.format(
            self.user, self.start_date, self.expire_date)

    def save(self, *args, **kwargs):
        if not self.expire_date:
            self.expire_date = self.start_date + timedelta(days=1)
        else:
            self.recalculate()
        super(Subscription, self).save(*args, **kwargs)

    def days(self):
        return (self.expire_date - self.start_date).days

    def recalculate(self):
        if self.plan.daily_fees:
            daily_fee = self.plan.price / self.plan.days
            days = self.payment_set.aggregate(Sum('value')).get(
                'value__sum', 0) / daily_fee
            self.expire_date = self.start_date + timedelta(days=days)
        else:
            self.expire_date = self.start_date + timedelta(days=self.plan.days)

    def credit(self):
        if self.plan.daily_fees:
            return self.payment_set.aggregate(Sum('value')).get(
                'value__sum', 0) - self.plan.price
        return 0


class Payment(models.Model):
    #TODO: error on try to pay for paid subscr
    administrant = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='payments')
    subscription = models.ForeignKey(Subscription)
    value = models.IntegerField()
    pay_date = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'Платеж'
        verbose_name_plural = u'Платежи'


class Visit(models.Model):
    administrant = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='visitors')
    subscription = models.ForeignKey(Subscription)
    arrival_time = models.DateTimeField(default=datetime.now())
    departure_time = models.DateTimeField(**nullable)
    pastimes = models.ManyToManyField('pastimes.Pastime', **nullable)

    class Meta:
        verbose_name = u'Визит'
        verbose_name_plural = u'Визиты'

    def __unicode__(self):
        return u'{0} {1}'.format(self.subscription.user, self.arrival_time)


@receiver(post_save, sender=Payment)
def recalculate_subscription(sender, **kwargs):
    subscription = kwargs['instance'].subscription
    subscription.recalculate()
    subscription.save()
