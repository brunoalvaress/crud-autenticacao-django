from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import persons_list, person_new, person_update, person_delete

urlpatterns = [
    path('list/', persons_list, name='persons_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id>/', person_update, name='person_update'),
    path('delete/<int:id>/', person_delete, name='person_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)