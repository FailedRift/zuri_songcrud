from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from musicapp.models import Artiste
from musicapp.serializers import ArtisteSerializer


# Create your views here.
class ListArtisteAPIView(ListAPIView):
    """This endpoint list all of the available Artistes from the database"""
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class CreateArtisteAPIView(CreateAPIView):
    """This endpoint allows for creation of a Artiste"""
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class UpdateArtisteAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Artiste by passing in the id of the todo to update"""
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class DeleteArtisteAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Artiste from the database"""
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

