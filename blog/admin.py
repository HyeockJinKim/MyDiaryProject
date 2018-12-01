from django.contrib import admin

# Register your models here.
from blog.models import WithMe, Subject, Location, Tag, Diary

admin.site.register(WithMe)
admin.site.register(Subject)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(Diary)