from .models import Collection
from .serializers import CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class CollectionList(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass


class CollectionDetail(APIView):

    def get_collection(self, pk):
        pass

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
