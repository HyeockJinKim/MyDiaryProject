from rest_framework import serializers

from blog.models import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        exclude = ('created',)
