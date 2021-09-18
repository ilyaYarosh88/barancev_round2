# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    if app.groupFixture.group_count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = app.groupFixture.get_group_list()
    app.groupFixture.delete_first_group()
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

