from model.contact import Contact


def test_modify_first_contact(app):
#    if app.contact.count() == 0:
#        app.contact.add_new_contact(Contact(name="Agata", surname="K."))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(name="Modified name", surname="Modified surname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

