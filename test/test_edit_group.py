from model.group import Group
from random import randrange



def test_modify_group_name(app):
    if app.groupFixture.group_count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = app.groupFixture.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="EditedGroup", header="EditedHeader", footer="EditedFooter")
    group.id = old_groups[index].id
    app.groupFixture.edit_group_by_index(index, group)
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)











