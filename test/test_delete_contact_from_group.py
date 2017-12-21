from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, orm, check_ui):
    groups = [i for i in orm.get_group_list() if i.name != ""]
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        groups = orm.get_group_list()
    group = random.choice(groups)

    contacts_in_group = orm.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        contacts = orm.get_contact_list()
        if len(contacts) == 0:
            app.contact.add_new_contact(Contact(firstname="test"))
            contacts = orm.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact, group)
        contacts_in_group = orm.get_contacts_in_group(group)
    else:
        app.contact.select_group(group)
    contact_to_delete = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(contact_to_delete, group)
    contacts_in_group.remove(contact_to_delete)
    new_contact_list = orm.get_contacts_in_group(group)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)