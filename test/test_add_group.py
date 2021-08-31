# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from fixture.application import Application


#инициализируем фикстуру
@pytest.fixture
def app(request):
    fixture = Application()
#Для разрушения фикстуры специальный параметр с особым методом
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.groupFixture.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    app.sessionFixture.logout()

def test_add_empty_group(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.groupFixture.create(Group(name="", header="", footer=""))
    app.sessionFixture.logout()



