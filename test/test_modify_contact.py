from model.contact import Contact
from random import randrange


def test_modify_some_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(name="Agata", surname="K."))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="Modified name", surname="Modified surname")
    contact.surname = old_contacts[index].surname
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.surname_or_max) == sorted(new_contacts, key=Contact.surname_or_max)


