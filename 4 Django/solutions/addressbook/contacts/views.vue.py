from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

import json

from .models import AddressContact

# Create your views here.
def index(request):

    addresses = AddressContact.objects.order_by('-last_name')
    context = {
        'contacts': addresses
    }

    # return HttpResponse('Hello World!')
    return render(request, 'contacts/index.html', context)

def add_contact(request):  
    # return HttpResponse('Add contact')
    return render(request, 'contacts/add_contact.html')

def save_contact(request):
    print(request.POST)
    contacts = request.POST

    output = AddressContact(
        first_name=contacts['first-name'],
        last_name=contacts['last-name'],
        email=contacts['email'],
        phone_number=contacts['phone-number'],
        address=contacts['address']
    )
    output.save()
    return HttpResponseRedirect(reverse('contacts:index'))

def edit_contact(request, contact_id):
    contact = get_object_or_404(AddressContact, pk=contact_id)

    if request.method == 'GET':

        # return HttpResponse(f'Id: {contact_id}')
        return render(request, 'contacts/edit_contact.html', {'contact': contact})
    elif request.method == "POST":
        contact.first_name = request.POST['first-name']
        contact.last_name = request.POST['last-name']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']

        contact.save()
        return HttpResponseRedirect(reverse('contacts:index'))


def delete_contact(request, contact_id):
    contact = get_object_or_404(AddressContact, pk=contact_id)

    contact.delete()

    return HttpResponseRedirect(reverse('contacts:index'))


def get_contacts(request):
    contacts = AddressContact.objects.all()

    print(contacts)
    output = []
    for contact in contacts:
        output.append({
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'address': contact.address,
            'phone_number': contact.phone_number,
            'email': contact.email
        })

    print(output)
    return JsonResponse(output, safe=False)