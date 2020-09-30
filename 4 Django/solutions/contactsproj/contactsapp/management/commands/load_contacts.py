from django.core.management.base import BaseCommand
import requests
from contactsapp.models import Contact
from datetime import datetime

# https://randomuser.me/documentation
class Command(BaseCommand):

    def handle(self, *args, **options):
        Contact.objects.all().delete() # wipe the table
        response = requests.get('https://randomuser.me/api/?results=100&nat=us')
        data = response.json()
        # print(data)
        for contact_data in data['results']:
            first_name = contact_data['name']['first']
            last_name = contact_data['name']['last']
            phone_number = contact_data['phone']
            email = contact_data['email']
            # 3333 New Brighton Road, Portland Oregon 97214, USA
            address = str(contact_data['location']['street']['number']) + ' ' + contact_data['location']['street']['name'] + ', ' + contact_data['location']['city'] + ' ' + contact_data['location']['state'] + ' ' + str(contact_data['location']['postcode']) + ', ' + contact_data['location']['country']
            birthday = contact_data['dob']['date']
            birthday = birthday[:len(birthday)-5]
            birthday = datetime.strptime(birthday, '%Y-%m-%dT%H:%M:%S')

            contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, address=address, birthday=birthday)
            contact.save()
        
        

        