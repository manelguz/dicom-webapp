from django.urls import path
from .views import ImageAPIView, ImageAPIList

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('id/<id>', ImageAPIView.as_view()),
    path('list', ImageAPIList.as_view()),
]