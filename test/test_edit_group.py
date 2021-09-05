from model.group import Group



def test_modify_group_name(app):
    if app.groupFixture.count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    app.groupFixture.edit_first_group(Group(name="EditedName"))




def test_modify_group_header(app):
    if app.groupFixture.count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    app.groupFixture.edit_first_group(Group(header="EditedHeader"))


def test_modify_group_footer(app):
    if app.groupFixture.count() == 0:
        app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    app.groupFixture.edit_first_group(Group(footer="EditedFooter"))
