from django.db import models
from django.contrib.gis.db import models


class TreesData(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    str_schl = models.CharField(max_length=5, blank=True, null=True)
    baumgruppe = models.CharField(max_length=50, blank=True, null=True)
    watering = models.BooleanField(default = False)
    fruit = models.BooleanField(default = False)
    eichenprozessionsspinner = models.BooleanField(default = False)
    date_water = models.DateField()
	

    class Meta:
        managed = False
        db_table = 'trees_data'
		

class Userdata(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(max_length=50, blank=True, null=True)
	feedback = models.CharField(max_length=500, blank=True, null=True)
	entry_date = models.DateField()
	tree_reference = models.IntegerField()
	
	class Meta:
		managed = False
		db_table = 'userdata'