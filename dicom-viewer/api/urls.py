from django.urls import path
from .views import ImageAPIView, ImageAPIList

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('id/<id>', ImageAPIView.as_view()), # get/delete images with the given id
    path('list', ImageAPIList.as_view()), # path to list the images
]