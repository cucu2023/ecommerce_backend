from django.shortcuts import render
from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


class CategoriaListCreateView(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDeleteView(APIView):
    def delete(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
