from model.group import Group



def test_modify_group_name(app):
    if app.groupFixture.group_count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = app.groupFixture.get_group_list()
    app.groupFixture.edit_first_group(Group(name="EditedName"))
    new_groups = app.groupFixture.get_group_list()
    assert len(old_groups) == len(new_groups)





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
