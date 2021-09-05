# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    if app.groupFixture.group_count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    app.groupFixture.delete_first_group()


