from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm, check_ui):
    contacts = orm.get_contact_list()
    if len(contacts) == 0:
        app.contact.add_new_contact(Contact(firstname="test"))
        contacts = orm.get_contact_list()
    contact = random.choice(contacts)

    groups = orm.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
        groups = orm.get_group_list()
    group = random.choice(groups)
    contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    contacts_in_group.append(contact)
    assert sorted(contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_contacts_in_group, key=Group.id_or_max) == sorted(app.contact.get_contact_list(),key=Group.id_or_max)