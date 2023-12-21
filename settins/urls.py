# proyekt/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),  # your_app_name o'rniga loyihangizning nomini yozing
]
