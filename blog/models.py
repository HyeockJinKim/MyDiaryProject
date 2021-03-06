from django.db import models
from django.utils import timezone


class WithMe(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()

    @staticmethod
    def get_name(pk):
        try:
            return WithMe.objects.get(pk=pk).name
        except:
            return None


class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    @staticmethod
    def get_name(pk):
        try:
            return Subject.objects.get(pk=pk).name
        except:
            return None


class Location(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    @staticmethod
    def get_name(pk):
        try:
            return Location.objects.get(pk=pk).name
        except:
            return None


class Tag(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    @staticmethod
    def get_name(pk):
        try:
            return Tag.objects.get(pk=pk).name
        except:
            return None


class Diary(models.Model):
    title = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)  # Null: 특별한 주제 없음
    post = models.TextField()
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)  # Null: 알 수 없는 장소
    with_me = models.ManyToManyField(WithMe)
    tags = models.ManyToManyField(Tag)
    date = models.DateField(default=timezone.localdate)
