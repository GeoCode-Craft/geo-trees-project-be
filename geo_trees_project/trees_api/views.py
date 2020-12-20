from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry,Point
from . models import  TreesData
from . serializers import  TreesDataSerializer
class TreesDataViewSet(viewsets.ModelViewSet):
	serializer_class = TreesDataSerializer
	queryset =TreesData.objects.all()


