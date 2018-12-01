
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from django.contrib.auth import views as auth_views
from home import urls as home_urls

urlpatterns = [
    path('clientes/', include(clientes_urls)),
    path('', include(home_urls)),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
