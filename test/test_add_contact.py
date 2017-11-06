# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login2(username="admin", password="secret")
    app.contact.add_new_contact(Contact(name="Agata", surname="Kłopotowska"))
    app.session.logout2()

def test_add_empty_contact(app):
    app.session.login2(username="admin", password="secret")
    app.contact.add_new_contact(Contact(name="", surname=""))
    app.session.logout2()
