# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login2(username="admin", password="secret")
    app.group.create(Group(name="gr", header="gr", footer="gr"))
    app.session.logout2()


def test_add_empty_group(app):
    app.session.login2(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout2()

