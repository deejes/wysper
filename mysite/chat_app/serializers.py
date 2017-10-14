from restframework import serializer
from .models import Message

class MessageSerializer(serializer.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
