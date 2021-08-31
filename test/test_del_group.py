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


def test_delete_first_group(app):
    app.sessionFixture.login(username="admin", password="secret")
    app.groupFixture.delete_first_group()
    app.sessionFixture.logout()

