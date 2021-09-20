from model.group import Group



def test_modify_group_name(app):
    if app.groupFixture.group_count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = app.groupFixture.get_group_list()
    group = Group(name="EditedGroup", header="EditedHeader", footer="EditedFooter")
    group.id = old_groups[0].id
    app.groupFixture.edit_first_group(group)
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)







def test_modify_group_header(app):
    if app.groupFixture.group_count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = app.groupFixture.get_group_list()
    app.groupFixture.edit_first_group(Group(header="EditedHeader"))
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.groupFixture.group_count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = app.groupFixture.get_group_list()
    app.groupFixture.edit_first_group(Group(footer="EditedFooter"))
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) == len(new_groups)
