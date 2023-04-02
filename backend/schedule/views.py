from django.shortcuts import render
from django.views.generic import TemplateView,  ListView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import ScheduleSerializers
from .models import Schedule, GroupSchedule
from rest_framework.renderers import TemplateHTMLRenderer




class ScheduleMain(ListAPIView):
    serializer_class = ScheduleSerializers
    renderer_classes = [TemplateHTMLRenderer, ]
    queryset = Schedule.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        print(queryset.values())
        return Response({'schedule' : queryset, "group": GroupSchedule.objects.all()}, template_name="base.html") 
        
   


            
class ScheduleGroupDetail(ListAPIView):
    serializer_class = ScheduleSerializers
    renderer_classes = [TemplateHTMLRenderer, ]
    queryset = Schedule.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(group__pk=self.kwargs['id_group'])
        print(queryset.values())
        return Response({'schedule' : queryset, "group": GroupSchedule.objects.all()}, template_name="base.html") 