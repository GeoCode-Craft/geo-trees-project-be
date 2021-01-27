from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry,Point
from . models import  TreesData, Userdata
from . serializers import  TreesDataSerializer, UserDataSerializer

class TreesDataViewSet(viewsets.ModelViewSet):
	serializer_class = TreesDataSerializer
	queryset = TreesData.objects.all()


class UserDataViewSet(viewsets.ModelViewSet):
	serializer_class = UserDataSerializer
	queryset = Userdata.objects.all()
