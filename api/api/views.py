
from wsgiref.util import FileWrapper
from api.custom_render import JPEGRenderer, PNGRenderer
from rest_framework import generics
from images.models import Images
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from PIL import Image


class ImageAPIView(generics.RetrieveAPIView):

    queryset = Images.objects.filter(id=1)
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        renderer_classes = [JPEGRenderer]
        queryset = Images.objects.get(id=self.kwargs['id']).image
        data = queryset
        return Response(data, content_type='image/jpg')