# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.groupFixture.get_group_list()
    app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.groupFixture.get_group_list()
    app.groupFixture.create(Group(name="", header="", footer=""))
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)



