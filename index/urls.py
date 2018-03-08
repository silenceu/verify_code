from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check', views.check, name='check')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)