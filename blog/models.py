from django.db import models


# Create your models here.
class WithMe(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()


class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


class Location(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


class Diary(models.Model):
    title = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)  # Null: 특별한 주제 없음
    post = models.TextField()
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)  # Null: 알 수 없는 장소
    with_me = models.ManyToManyField(WithMe)
    created = models.DateTimeField(auto_now_add=True)
