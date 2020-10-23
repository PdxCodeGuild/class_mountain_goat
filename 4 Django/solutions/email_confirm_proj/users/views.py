from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import User, EmailConfirmation
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta

import django.contrib.auth


import string
import random

def random_code(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(n)])

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)

        django.contrib.auth.login(request, user)

        email_confirmation = EmailConfirmation(user=user, code=random_code(10))
        email_confirmation.save()

        body = render_to_string('users/email.html', {'code': email_confirmation.code, 'domain': 'http://' + request.META['HTTP_HOST']})
        print(body)
        send_mail('Confirm Your Account', '', 'NunyaBusinessSHA132@gmail.com', [email], fail_silently=False, html_message=body)

        return HttpResponseRedirect(reverse('users:confirm'))

    username = 'user' + str(User.objects.count() + 1)
    return render(request, 'users/register.html', {'username': username})

def confirm(request):

    code = request.GET.get('code', '')
    if code == '':
        return render(request, 'users/confirm.html', {})

    # check if there exists an email confirmation with the given code made in the last day
    yesterday = timezone.now() - timedelta(days=1)
    print(yesterday)
    email_confirmation = EmailConfirmation.objects.filter(code=code, date_created__gt=yesterday).first()
    # if there isn't, render the template with a 'resend confirmation' button
    if email_confirmation is None:
        return render(request, 'users/confirm.html', {})
    # otherwise mark it as confirmed
    email_confirmation.date_confirmed = timezone.now()
    email_confirmation.save()

    email_confirmation.user.email_address_confirmed = True
    email_confirmation.user.save()

    return HttpResponseRedirect(reverse('users:home'))

def home(request):

    # if request.user.email_confirmations.filter(date_confirmed__isnull=False).exists():

    if not request.user.email_address_confirmed:
        return HttpResponseRedirect(reverse('users:confirm'))
    

    return render(request, 'users/home.html', {})


