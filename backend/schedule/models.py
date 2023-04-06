from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser




class TimeSchedule(models.Model):
    time =models.CharField(verbose_name="Время", max_length=30)
    
    def __str__(self) -> str:
        return self.time
    
    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'



class LessonSchedule(models.Model):
    lesson = models.CharField(max_length=70, verbose_name="Название предмета")
    
    def __str__(self) -> str:
        return self.lesson
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class GroupSchedule(models.Model):
    group = models.CharField(max_length=70, verbose_name="Группа")
    
    def __str__(self) -> str:
        return self.group
    
    def get_absolute_url(self):
        return reverse("group_detail", kwargs={"id_group": self.pk})
    
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    
    
class Schedule(models.Model):
    time = models.ForeignKey(TimeSchedule, related_name="schedule_time", on_delete=models.CASCADE)
    group = models.ForeignKey(GroupSchedule, related_name="schedule_group", on_delete=models.CASCADE)
    lessons = models.ManyToManyField(LessonSchedule,  related_name="schedule_lessons")
    
    created = models.DateField(auto_now_add=True, verbose_name="Дата", )
    
    
    def __str__(self) -> str:
        return f"{self.time}, {self.group}, {self.lessons}, {self.created}"
    
    
    class Meta:
        verbose_name = 'Раписание группы'
        verbose_name_plural = 'Раписание групп'
    
    
class User(AbstractUser):
    patronymic = models.CharField('Отчество', max_length=255)
    group = models.ForeignKey(GroupSchedule, related_name="user_group", on_delete=models.CASCADE, null=True, blank=True)