from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('backend/', include('chevrolet.urls')),
    path('kostyum/', include('ferrari.urls')),
    path('kostyum/', include('kamaro.urls')),
    path('kostyum/', include('lamborgini.urls')),
    path('kostyum/', include('mustang.urls')),
    path('kostyum/', include('tesla.urls')),
    path('kostyum/', include('about.urls')),
    path('kostyum/', include('wolksvagen.urls')),
]
