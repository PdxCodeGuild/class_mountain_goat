from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path("", views.index, name="index"),
    path("add_contact/", views.add_contact, name="add"),
    path("save_contact/", views.save_contact, name="save"),
    path("edit_contact/<int:contact_id>/", views.edit_contact, name="edit"),
    path("delete_contact/<int:contact_id>/", views.delete_contact, name="delete"),
    # path("api/contacts/", views.get_contacts, name="get_contacts")
]
