# -*- coding: utf-8 -*-
from django.db import models


class Devotional(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=128)
    body = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.title, self.date)