from django.urls import path
from .views import ImageAPIView

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('id/<id>', ImageAPIView.as_view()),
]