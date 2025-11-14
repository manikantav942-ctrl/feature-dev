from django.urls import path
from .views import SimpleAPIView

urlpatterns = [
    path('simple/', SimpleAPIView.as_view(), name='simple_api'),
]