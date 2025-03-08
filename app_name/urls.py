from django.urls import path
from .views import echo_params
# Create your views here.

urlpatterns = [
    path('echo/', echo_params, name='echo-params'),
]