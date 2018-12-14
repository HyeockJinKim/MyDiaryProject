from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.DiaryListCreate.as_view()),
    # path('edit_post/', views.edit),
    path('new', views.new, name='new'),
    path('tags', views.tags, name='tags')
]
