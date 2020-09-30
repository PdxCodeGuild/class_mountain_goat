from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Contact
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    contacts = Contact.objects.all().order_by('last_name')
    search = request.GET.get('search', '')
    if search != '':
        # search in one field
        # contacts = contacts.filter(first_name__icontains=search)
        # search for term in first_name AND last_name
        # contacts = contacts.filter(first_name__icontains=search, last_name__icontains=search)

        contacts = contacts.filter(Q(first_name__icontains=search)
                                    | Q(last_name__icontains=search)
                                    | Q(phone_number__icontains=search))
                                    # | Q(email__icontains=search)
                                    # | Q(address__icontains=search))
    
    # d = {'apples': 1, 'bananas': 2}
    # print(d.get('cherries', 3))

    # get the page if it was specified in the query string
    # or get 1 if it isn't
    page_number = request.GET.get('page', 1)

    contacts_per_page = 10
    paginator = Paginator(contacts, contacts_per_page)
    contacts_page = paginator.page(page_number)

    context = {
        'message': 'contacts',
        'contacts': contacts_page,
        'search': search,
    }
    print(context)
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



