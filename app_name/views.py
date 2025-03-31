from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .models import Personas
from .serializers import PersonasSerializer
from rest_framework import viewsets, status # Importamos viewsets
from rest_framework.decorators import action


import logging
logger = logging.getLogger('django')
logger.setLevel(logging.INFO)



class PersonasViewSet(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

    @extend_schema(
        operation_id="custom_create_persona",
        request=PersonasSerializer,  # Estructura esperada
        responses={
            201: OpenApiResponse(description="Persona creada correctamente"),
            400: OpenApiResponse(description="Error en la solicitud"),
        },
        summary="Crear una nueva persona",
        description="Permite crear una nueva persona enviando nombre y apellidos."
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

