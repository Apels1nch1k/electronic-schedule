# Generated by Django 4.1.7 on 2023-04-01 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_group', to='schedule.groupschedule'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='lessons',
            field=models.ManyToManyField(related_name='schedule_lessons', to='schedule.lessonschedule'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_time', to='schedule.timeschedule'),
        ),
    ]