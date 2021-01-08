from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import  TreesData

class TreesDataSerializer(GeoFeatureModelSerializer):
    
	class Meta:
		model = TreesData
		fields = '__all__'
		geo_field = 'geom'