from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *


def home(request):
    form_contact = ContactForm()
    form_order = OrderForm()
    if request.method == 'POST':
        if 'contact_form' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                if Contact.objects.filter(phone=phone).exists():
                    messages.error(
                        request, 'Ошибка: данный номер телефона уже зарегистрирован')
                else:
                    Contact.objects.create(name=name, phone=phone)
                    messages.success(
                        request, 'Форма отправлена успешно')
            else:
                messages.error(
                    request, 'Заполните все обязательные поля')

        elif 'order_form' in request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                budget = form.cleaned_data['budget']
                task = form.cleaned_data['task']
                if Contact.objects.filter(phone=phone).exists():
                    messages.error(
                        request, 'Ошибка: данный номер телефона уже зарегистрирован')
                else:
                    Order.objects.create(
                        name=name, phone=phone, email=email, budget=budget, task=task)
                    messages.success(
                        request, 'Форма отправлена успешно')
            else:
                messages.error(
                    request, 'Заполните все обязательные поля!')

        else:
            context = {'form_contact': form_contact, 'form_order': form_order}
            return render(request, 'marketing_site/home.html', context)
    context = {
        'title': 'Главная',
        'form_contact': form_contact,
        'form_order': form_order,
    }
    return render(request, 'marketing_site/home.html', context)


def privacy(request):
    return render(request, 'marketing_site/privacy.html', {'title': 'Правила обработки персональных данных'})


def about(request):
    services = Service.objects.all()
    context = {
        'title': 'О нас',
        'services': services
    }
    return render(request, 'marketing_site/about.html', context)


def services(request):
    services = Service.objects.all()
    context = {
        'title': 'Услуги',
        'services': services
    }
    return render(request, 'marketing_site/services.html', context)


def projects(request):
    projects = Project.objects.all()
    context = {
        'title': 'Наши работы',
        'projects': projects
    }
    return render(request, 'marketing_site/projects.html', context)
