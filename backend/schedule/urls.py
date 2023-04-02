from django.urls import path, include
from .views import *
urlpatterns = [
    path('', ScheduleMain.as_view(), name="schedule"),
    path('<int:id_group>', ScheduleGroupDetail.as_view(), name="group_detail")
]