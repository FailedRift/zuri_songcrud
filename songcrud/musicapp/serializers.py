from django.db.models import fields
from rest_framework import serializers
from musicapp.models import Artiste

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"