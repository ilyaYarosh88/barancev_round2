from model.group import Group
import pytest
from fixture.application import Application


fixture = None

#инициализируем фикстуру
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.sessionFixture.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.sessionFixture.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.sessionFixture.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

