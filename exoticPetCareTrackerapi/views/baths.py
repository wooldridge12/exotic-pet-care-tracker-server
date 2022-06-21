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
        )    
        return Response(serializer.data)
    
    def create(self, request):
        
        bath = Bath()
        bath.duration = request.data["duration"]
        bath.time = request.data["time"]
        bath.notes = request.data["notes"]
        
        try:
            bath.save()
            serializer = BathSerializer(bath, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        try:
            bath = Bath.objects.get(pk=pk)
            bath.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Bath.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class BathSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bath
        fields = ('id', 'duration', 'time', 'notes')
        
        depth = 1
        
        # Remember User is not used yet this is for setup.