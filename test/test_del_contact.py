

def test_delete_first_group(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.contactFixture.delete_first_contact()
    app.sessionFixture.logout()