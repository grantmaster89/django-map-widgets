from __future__ import unicode_literals

from django.contrib.gis.db import models


class PointField(models.Model):
    name = models.CharField(max_length=255)
    localtion = models.PointField()

    def __unicode__(self):
        return self.name
