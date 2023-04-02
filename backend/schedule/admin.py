from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    filter_horizontal = ["lessons"]
    list_filter = ['group','created']

@admin.register(GroupSchedule)
class AdminGroupSchedule(admin.ModelAdmin):
    pass

@admin.register(LessonSchedule)
class AdminLessonSchedule(admin.ModelAdmin):
    pass


@admin.register(TimeSchedule)
class AdminTimeSchedule(admin.ModelAdmin):
    pass