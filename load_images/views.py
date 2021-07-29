from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ImageListView(APIView):

    def get(self, request):
        images = ImageDetail.objects.all()
        image_serializer = ImageDetailSerializer(images, many=True)

        return Response(image_serializer.data)