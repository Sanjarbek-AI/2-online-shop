# Generated by Django 3.2.6 on 2021-08-10 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20210810_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(verbose_name='Feedback')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('job', models.CharField(max_length=50, verbose_name='Job')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
