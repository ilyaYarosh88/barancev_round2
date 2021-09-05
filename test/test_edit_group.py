from model.group import Group



def test_modify_group_name(app):

    app.groupFixture.edit_first_group(Group(name="EditedGroup"))



def test_modify_group_header(app):

    app.groupFixture.edit_first_group(Group(header="EditedHeader"))


def test_modify_group_footer(app):

    app.groupFixture.edit_first_group(Group(footer="EditedFooter"))
