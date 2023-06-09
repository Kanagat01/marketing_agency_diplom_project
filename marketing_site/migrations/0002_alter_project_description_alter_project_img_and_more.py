# Generated by Django 4.1.7 on 2023-04-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(upload_to='marketing_sites/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='img',
            field=models.ImageField(upload_to='marketing_site/images/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
