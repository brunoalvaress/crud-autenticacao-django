
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import home

urlpatterns = [

    path('', home, name='home'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
