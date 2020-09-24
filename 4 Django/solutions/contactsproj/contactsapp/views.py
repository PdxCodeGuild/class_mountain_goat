from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Contact

def index(request):
    contacts = Contact.objects.all().order_by('last_name')
    # contacts = Contacts.objects.order_by('last_name')
    # contacts = Contacts.objects.filter(last_name='Smith')
    # contacts = Contacts.objects.filter(address__icontains='portland')
    # print(contacts[0].last_name)

    context = {
        'message': 'Contacts',
        'contacts': contacts
    }
    return render(request, 'contactsapp/index.html', context)


def about(request):
    return render(request, 'contactsapp/about.html')


def details(request, contact_id):
    # return HttpResponse(f'Contact with id {contact_id}')
    contact = get_object_or_404(Contact, pk=contact_id)

    # print(contact)
    context = {
        'contact': contact
    }

    return render(request, 'contactsapp/details.html', context)

def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()

    return redirect('contactsapp:index')



