from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('subdiscovery/', include('subdiscovery.urls')),
    path('admin/', admin.site.urls),
]
