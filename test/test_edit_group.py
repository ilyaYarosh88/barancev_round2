from model.group import Group



def test_edit_group(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.groupFixture.edit_first_group(Group(name="EditedGroup", header="EditedHeader", footer="EditedFooter"))
    app.sessionFixture.logout()