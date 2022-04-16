
from urllib import response
from wsgiref.util import FileWrapper
from api.custom_render import JPEGRenderer, PNGRenderer
from rest_framework import generics
from images.models import Images    
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse, HttpResponseNotFound
from django.core.exceptions import BadRequest



class ImageAPIView(generics.RetrieveAPIView):

    parser_classes = [MultiPartParser, FormParser]
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        try:
            data = Images.objects.get(name=self.kwargs['id']).image
        except Images.DoesNotExist:
            return HttpResponseNotFound("Image does not exist")
        return Response(data, content_type='image/jpg')

    def delete(self, request, *args, **kwargs):
        try:
            object_data = Images.objects.get(name=self.kwargs['id'])
        except Images.DoesNotExist:
            return HttpResponseNotFound("Image does not exist")
        object_data.image.delete()
        object_data.delete()
        return HttpResponse("Image Correctly deleted", content_type="text/plain")

    def post(self, request):
        file = request.data['file']
        name = request.data['name']
        if Images.objects.filter(name=name).exists():
            return HttpResponseBadRequest('The image already exist with this id.')
        Images.objects.create(image=file, name=name)
        return HttpResponse("Image Correctly updated", content_type="text/plain")

class ImageAPIList(generics.RetrieveAPIView):

    parser_classes = [MultiPartParser, FormParser]
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        data = Images.objects.all()
        image_names = [img.name for img in data]
        answ = {"all_images": image_names}
        return JsonResponse(answ)