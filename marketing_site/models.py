from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price_from = models.IntegerField()
    price_to = models.IntegerField()
    img = models.ImageField(upload_to='marketing_site/images/')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='marketing_site/images/')
    project_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    task = models.TextField()

    def __str__(self):
        return self.name
