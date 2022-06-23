from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from exoticPetCareTrackerapi.models import FoodType


class FoodTypeView(ViewSet):
    
    def list(self, request):
        
        foodtypes = FoodType.objects.all()
        
        serializer = FoodTypeSerializer(
            foodtypes, many=True, context={'request': request}
        )    
        return Response(serializer.data)
    
class FoodTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodType
        fields = ('id', 'label', 'food_type')