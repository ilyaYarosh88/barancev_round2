# -*- coding: utf-8 -*-
from group import Group
import pytest
from application import Application


#инициализируем фикстуру
@pytest.fixture
def app(request):
    fixture = Application()
#Для разрушения фикстуры специальный параметр с особым методом
    request.addfinalazer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()



