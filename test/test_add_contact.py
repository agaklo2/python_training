# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new_contact(Contact(name="Agata", surname="Kłopotowska"))


def test_add_empty_contact(app):
    app.contact.add_new_contact(Contact(name="", surname=""))

