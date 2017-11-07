# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login2(username="admin", password="secret")
    app.contact.add_new_contact(Contact(name="Agata", surname="Kłopotowska"))
    app.session.logout2()

def test_add_empty_contact(app):
    app.session.login2(username="admin", password="secret")
    app.contact.add_new_contact(Contact(name="", surname=""))
    app.session.logout2()
