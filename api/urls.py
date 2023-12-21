# urls.py
from django.urls import path
from .views import get_my_data_by_id


urlpatterns = [
    path('api/my-data/', get_my_data_by_id.as_view(), name='get_my_data_by_id'),
]
