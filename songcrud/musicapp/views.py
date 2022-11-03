from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Artiste
from .serializers import ArtisteSerializer

# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by First Name': '/?first_name=first_name',
        'Search by Last Name': '/?last_name=last_name',
        'Search by Age': '/?age=age',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/artiste/pk/delete'
    }
  
    return Response(api_urls)