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
