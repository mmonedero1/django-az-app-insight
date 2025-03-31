from rest_framework import serializers
from .models import Personas

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'  # O selecciona campos específicos: ['id_persona', 'nombre', 'apellidos']
