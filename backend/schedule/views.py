from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,  ListView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import ScheduleSerializers
from .models import Schedule, GroupSchedule, User
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic.edit import CreateView
from .forms import RegistrationForm, SingInForms
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView

class ScheduleMain(ListAPIView):
    serializer_class = ScheduleSerializers
    renderer_classes = [TemplateHTMLRenderer, ]
    queryset = Schedule.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        print(queryset.values())
        return Response({'schedule' : queryset, "group": GroupSchedule.objects.all()}, template_name="main.html") 
        
   


            
class ScheduleGroupDetail(ListAPIView):
    serializer_class = ScheduleSerializers
    renderer_classes = [TemplateHTMLRenderer, ]
    queryset = Schedule.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(group__pk=self.kwargs['id_group'])
        return Response({'schedule' : queryset, "group": GroupSchedule.objects.all(), "group_name" : GroupSchedule.objects.filter(id=self.kwargs['id_group'])}, template_name="main.html")



class Profil(APIView):
    serializer_class = ScheduleSerializers
    renderer_classes = [TemplateHTMLRenderer, ]

    
    def get(self, request, *args, **kwargs):
        print(request.user.group)
        queryset = Schedule.objects.filter(group=request.user.group).last()
        return Response({'schedule' : queryset}, template_name="profil.html")
    
class Registration(CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    def post(self, request):
        form = self.form_class(request.POST)
        print(form.errors)
        if form.is_valid():
            authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            form.save()
            return redirect('schedule')
        return render(request, self.template_name, {'form' : form})
    
class SingInView(LoginView):
    form_class = SingInForms
    template_name = "singin.html"
    def post (self, request):
        form = self.form_class(data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('schedule')
        return render(request, self.template_name, {'form' : form})
    

class Logout(LogoutView):
    pass