# -*- coding: utf-8 -*-

def test_delete_first_group(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.groupFixture.delete_first_group()
    app.sessionFixture.logout()

