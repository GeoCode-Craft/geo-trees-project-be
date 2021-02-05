from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry,Point
from . models import  TreesData, Userdata
from . serializers import  TreesDataSerializer, UserDataSerializer

#class TreesDataViewSet(viewsets.ModelViewSet):
#	serializer_class = TreesDataSerializer
#	queryset = TreesData.objects.all()
class TreesDataDetail(APIView):
    """
    Retrieve, update or delete a tree instance.
    """
    def get_object(self, pk):
        try:
            return TreesData.objects.get(pk=pk)
        except TreesData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tree = self.get_object(pk)
        serializer = TreesDataSerializer(tree)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tree = self.get_object(pk)
        serializer = TreesDataSerializer(tree, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tree = self.get_object(pk)
        tree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDataViewSet(viewsets.ModelViewSet):
	serializer_class = UserDataSerializer
	queryset = Userdata.objects.all()
