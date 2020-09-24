from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Contact
from datetime import datetime

def index(request):
    contacts = Contact.objects.all().order_by('last_name')
    # contacts = Contacts.objects.order_by('last_name')
    # contacts = Contacts.objects.filter(last_name='Smith')
    # contacts = Contacts.objects.filter(address__icontains='portland')
    # print(contacts[0].last_name)

    context = {
        'message': 'contacts',
        'contacts': contacts
    }
    return render(request, 'contactsapp/index.html', context)


def about(request):
    return render(request, 'contactsapp/about.html')


def details(request, contact_id):
    # print('~'*80)
    # print(request.method)
    # print(request.POST)
    # print('~'*80)
    # return HttpResponse(f'Contact with id {contact_id}')

    contact = get_object_or_404(Contact, pk=contact_id)
    message = request.GET.get('message', '')
    
    # print(contact)
    context = {
        'contact': contact,
        'message': message
    }
    return render(request, 'contactsapp/details.html', context)

def save(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    email = request.POST['email']
    address = request.POST['address']
    birthday = request.POST['birthday']
    birthday_vanilla = request.POST['birthday_vanilla']

    # https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-behavior
    birthday = datetime.strptime(birthday, '%b %d, %Y')
    # birthday_vanilla = datetime.strptime(birthday, '%Y-%m-%d')

    contact.first_name = first_name
    contact.last_name = last_name
    contact.phone_number = phone
    contact.email = email
    contact.address = address
    contact.birthday = birthday
    contact.save()

    return HttpResponseRedirect(reverse('contactsapp:details', args=(contact.id,))+'?message=success')




def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()

    # return redirect('contactsapp:index')
    return HttpResponseRedirect(reverse('contactsapp:index'))



