from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('line/', include('line.urls')),
    path('admin/', admin.site.urls),
]
