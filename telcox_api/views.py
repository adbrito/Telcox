from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteView(APIView):
    def get(self, request, cliente_id=None):
        if cliente_id:
            try:
                cliente = Cliente.objects.get(id=cliente_id)
                serializer = ClienteSerializer(cliente)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Cliente.DoesNotExist:
                return Response({"error": "Cliente not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            clientes = Cliente.objects.all()
            serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
