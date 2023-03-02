from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Personnage
from .serializers import PersonnageSerializer

class ApiView(APIView):

    #1. Affiche tous les éléments
    def get(self, request, *args, **kwargs):
        personnages = Personnage.objects.all()
        serializer = PersonnageSerializer(personnages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Créé un personnage
    def post(self, request, *args, **kwargs):
        data = {
            'nom': request.data.get('nom'), 
        }
        serializer = PersonnageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonnageDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Personnage.objects.get(id=id)
        except Personnage.DoesNotExist:
            return None

    # 3. Retrouve le personnage
    def get(self, request, id, *args, **kwargs):
        personnage_instance = self.get_object(id)
        if not personnage_instance:
            return Response(
                {"res": "Object with personnage id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PersonnageSerializer(personnage_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Met à jour le personnage
    def put(self, request, id, *args, **kwargs):
        personnage_instance = self.get_object(id)
        if not personnage_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nom': request.data.get('nom'), 
        }
        serializer = PersonnageSerializer(instance = personnage_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Supprime le personnage
    def delete(self, request, id, *args, **kwargs):
        personnage_instance = self.get_object(id)
        if not personnage_instance:
            return Response(
                {"res": "Object with personnage id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        personnage_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )