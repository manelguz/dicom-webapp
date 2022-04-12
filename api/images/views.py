from django.views import generic
from .models import Images


class ImagesListView(generic.ListView):
    model = Images
    template_name = 'images/all_images.html'
