# -*- coding: utf-8 -*-
from django.db import models

from utils.annoying import nullable


class Pastime(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(**nullable)

    class Meta:
        verbose_name = u'Времяпровождение'
        verbose_name_plural = u'Времяпровождения'

    def __unicode__(self):
        return self.name
