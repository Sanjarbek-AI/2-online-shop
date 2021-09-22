# Generated by Django 3.2.6 on 2021-08-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_testimonialmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialmodel',
            name='feedback_en',
            field=models.TextField(null=True, verbose_name='Feedback'),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='feedback_ru',
            field=models.TextField(null=True, verbose_name='Feedback'),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='feedback_uz',
            field=models.TextField(null=True, verbose_name='Feedback'),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='job_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Job'),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='job_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Job'),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='job_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='Job'),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='name_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
    ]
