from django.db import models
from django.contrib.gis.db import models


class TreesData(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    str_schl = models.CharField(max_length=5, blank=True, null=True)
    baumgruppe = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trees_data'