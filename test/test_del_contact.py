
def test_delete_first_contact(app):
    app.session.login2(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout2()