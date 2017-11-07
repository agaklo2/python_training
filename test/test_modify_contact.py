
def test_modify_first_contact(app):
    app.session.login2(username="admin", password="secret")
    app.contact.modify_first_contact()
    app.session.logout2()