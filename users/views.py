from rest_framework.views import APIView
from rest_framework.response import Response


class SimpleAPIView(APIView):
    def get(self, request):
        return Response({
            "message": "Hello from Django backend!",
            "status": "success"
        })