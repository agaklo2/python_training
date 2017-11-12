from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(name="Agata", surname="K."))
    app.contact.modify_first_contact(Contact(name="Modified name", surname="Modified surname"))
