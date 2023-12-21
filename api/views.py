# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyModel
from .serializers import MyModelSerializer

class get_my_data_by_id(APIView):
    def get(self, request, *args, **kwargs):
        try:
            my_data = MyModel.objects.get(id=1)  # Ma'lumotni olish, misol uchun ID=1
            serializer = MyModelSerializer(my_data)
            return Response(serializer.data)
        except MyModel.DoesNotExist:
            return Response({"error": "Malumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
