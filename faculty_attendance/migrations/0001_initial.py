# Generated by Django 4.2.21 on 2025-06-20 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PRESENT', 'Present'), ('LATE', 'Late'), ('ABSENT', 'Absent'), ('ON_LEAVE', 'On Leave')], default='PRESENT', max_length=20)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.class')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.faculty')),
            ],
            options={
                'ordering': ['-date', '-time_in'],
                'unique_together': {('faculty', 'class_instance', 'date')},
            },
        ),
        migrations.CreateModel(
            name='AttendanceSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('class_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.class')),
            ],
            options={
                'unique_together': {('class_instance', 'day_of_week')},
            },
        ),
    ]
