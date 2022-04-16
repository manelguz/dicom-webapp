
from rest_framework import generics
from images.models import Images    
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse, HttpResponseNotFound
import base64


class ImageAPIView(generics.RetrieveAPIView):

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        try:
            data = Images.objects.get(name=self.kwargs['id']).file_dicom
        except Images.DoesNotExist:
            return HttpResponseNotFound("Image does not exist")
        dicom_img = data.read()
        dicom_img_encoded = base64.b64encode(dicom_img).decode('utf-8')
        return JsonResponse({'dicom_img': dicom_img_encoded})

    def delete(self, request, *args, **kwargs):
        try:
            object_data = Images.objects.get(name=self.kwargs['id'])
        except Images.DoesNotExist:
            return HttpResponseNotFound("Image does not exist")
        object_data.image.delete()
        object_data.file_dicom.delete()
        object_data.delete()
        return HttpResponse("Image Correctly deleted", content_type="text/plain")

    def post(self, request):
        file = request.data['file']
        name = request.data['name']
        if Images.objects.filter(name=name).exists():
            return HttpResponseBadRequest('The image already exist with this id.')
        Images.objects.create(image=file, name=name, file_dicom=file)
        return HttpResponse("Image Correctly updated", content_type="text/plain")

class ImageAPIList(generics.RetrieveAPIView):

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        data = Images.objects.all()
        image_names = [img.name for img in data]
        answ = {"all_images": image_names}
        return JsonResponse(answ)