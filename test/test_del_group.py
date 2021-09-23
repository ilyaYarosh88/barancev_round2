# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.groupFixture.group_count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = app.groupFixture.get_group_list()
    index = randrange(len(old_groups))
    app.groupFixture.delete_group_by_index(index)
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups


