from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', project),
    path('', project_index, name='project_index'),
    path('<int:pk>/', project_detail, name='project_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)