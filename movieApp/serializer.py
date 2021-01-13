from rest_framework.serializers import ModelSerializer

from .models import Movies

class MoviesSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'body', 'created_at','updated_at')
        model = Movies