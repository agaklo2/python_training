from model.contact import Contact
import random


def test_modify_some_contact_name(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    modified_contact_name = Contact(firstname="Modified firstname", lastname="dfd")
    app.contact.modify_contact_by_id(contact.id, modified_contact_name)
    new_contacts = db.get_contact_by_id(contact.id)
    contact.firstname = str("Modified firstname")
    contact.lastname = str("dfd")
    assert contact == new_contacts


