from django.urls import path, include
from .views import  PersonasViewSet
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
# Create your views here.
router = DefaultRouter()
router.register(r'personas', PersonasViewSet)

urlpatterns = [
    # path('echo/', echo_params, name='echo-params'),
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),    
]