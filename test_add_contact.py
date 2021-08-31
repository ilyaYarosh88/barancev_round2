# -*- coding: utf-8 -*-
from contact import Contact
import pytest
from application import Application
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



#инициализируем фикстуру
@pytest.fixture
def app(request):
    fixture = Application()
#Для разрушения фикстуры специальный параметр с особым методом
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="Ivan", middlename="Sergeevich", lastname="Petrov", nickname="Butthead",
                            title="test", company="Gazprom", address="Moscow", home="+74950000000",
                            mobile="+79190000000", work="+74951000000", fax="+74952000000",
                            email="ispetrov@mail.ru", email2="ispetrov2@mail.ru", email3="ispetrov3@mail.ru",
                            homepage="www.petrov.su", bday="2", bmonth="April", byear="1973", aday="6", amonth="May",
                            ayear="1999", address2="Moscow", phone2="1", notes="Test"))
    app.logout()



