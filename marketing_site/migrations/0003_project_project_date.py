# Generated by Django 4.1.7 on 2023-04-06 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketing_site', '0002_alter_project_description_alter_project_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
