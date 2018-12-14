from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.DiaryListCreate.as_view()),
    # path('edit_post/', views.edit),
    path('new', views.new, name='new'),
    path('page/', views.page, name='page'),
    path('page/<int:pk>', views.page, name='page'),
    path('tags', views.tags, name='tags')
]
