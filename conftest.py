from model.group import Group
import pytest
from fixture.application import Application

#инициализируем фикстуру
@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.sessionFixture.login(username="admin", password="secret")
#Для разрушения фикстуры специальный параметр с особым методом
    def fin:
        fixture.sessionFixture.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
