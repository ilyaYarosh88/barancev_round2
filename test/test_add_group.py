# -*- coding: utf-8 -*-
from model.group import Group
from sys import maxsize

def test_add_group(app):
    old_groups = app.groupFixture.get_group_list()
    group = Group(name="Test_name", header="Test_header", footer="Test_footer")
    app.groupFixture.create(group)
    assert len(old_groups) + 1 == app.groupFixture.group_count()
    new_groups = app.groupFixture.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_empty_group(app):
#    old_groups = app.groupFixture.get_group_list()
#   group = Group(name="", header="", footer="")
#    app.groupFixture.create(group)
#   new_groups = app.groupFixture.get_group_list()
#   assert len(old_groups) + 1 == len(new_groups)
#   old_groups.append(group)
#   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


