import json

from django import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from blog.forms import DiaryForm
from blog.models import Diary, Subject, Location, WithMe, Tag
from blog.serializers import DiarySerializer


def index(request):
    # my_diary = Diary.objects.order_by('-id')[:5]
    return render(request, 'blog/index.html', locals())


class DiaryListCreate(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


def edit(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            return redirect(reverse('index'))

    form = DiaryForm()
    return render(request, 'blog/edit_post.html', locals())


@csrf_exempt
def new(request):
    data = json.loads(request.body.decode('utf-8'))
    # try:
    #     diary = Diary.objects.create(
    #         title=data['header'],
    #         subject=Subject.objects.get(name=data['subject']),
    #         post=data['content'],
    #         location=Location.objects.get(name=data['location']),
    #     )
    # except:
    #     return JsonResponse('create error')
    # try:
    #     for me in data['with_me']:
    #         diary.with_me.add(WithMe.objects.get(name=me))
    # except:
    #     return JsonResponse('with me error')
    # try:
    #     for tag in data['tags']:
    #         diary.tags.add(Tag.objects.get(name=tag))
    # except:
    #     return JsonResponse('tag error')
    return JsonResponse(data)
