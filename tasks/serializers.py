from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Tasks
        fields = ['name', 'description', 'id']
