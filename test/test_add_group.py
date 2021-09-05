# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):

    app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    app.sessionFixture.logout()

def test_add_empty_group(app):

    app.groupFixture.create(Group(name="", header="", footer=""))




