

def test_delete_first_group(app):

    app.contactFixture.delete_first_contact()
    app.sessionFixture.logout()