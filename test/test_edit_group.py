from model.group import Group



def test_modify_group_name(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.groupFixture.edit_first_group(Group(name="EditedGroup"))
    app.sessionFixture.logout()


def test_modify_group_header(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.groupFixture.edit_first_group(Group(header="EditedHeader"))
    app.sessionFixture.logout()

def test_modify_group_footer(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.groupFixture.edit_first_group(Group(footer="EditedFooter"))
    app.sessionFixture.logout()