from rest_framework.serializers import ModelSerializer
from .models import *

class SerializerMachine(ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'