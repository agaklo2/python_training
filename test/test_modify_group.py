from model.group import Group
import random

def test_modify_some_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    modified_group_name = Group(name="Modified group")
    app.group.modify_group_by_id(group.id, modified_group_name)
    new_group = db.get_group_by_id(group.id)
    group.name = str("Modified group")
    assert group == new_group


#def test_modify_first_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)