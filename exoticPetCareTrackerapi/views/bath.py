from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from exoticPetCareTrackerapi.models import Bath


class BathView(ViewSet):
    
    def list(self, request):
        
        baths = Bath.objects.all()
        
        serializer = BathSerializer(
            baths, many=True, context={'request': request}
        return Response(serializer.data)
        )    
        
        
class BathSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bath
        fields = ('id', 'duration', 'time', 'notes')
        
        depth = 1
        
        # Remember User is not used yet this is for setup.