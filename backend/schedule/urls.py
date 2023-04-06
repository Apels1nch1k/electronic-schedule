from django.urls import path, include
from .views import *
urlpatterns = [
    path('', ScheduleMain.as_view(), name="schedule"),
    path('<int:id_group>', ScheduleGroupDetail.as_view(), name="group_detail"),
    path('registration', Registration.as_view(), name="registration"),
    path('singin', SingInView.as_view(), name="singin"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('profil', Profil.as_view(), name="profil"),
    
]