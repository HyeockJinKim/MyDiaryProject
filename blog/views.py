from django.shortcuts import render
from rest_framework import generics
from blog.models import Diary
from blog.serializers import DiarySerializer


def index(request):
    return render(request, 'blog/index.html', locals())


class DiaryListCreate(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
