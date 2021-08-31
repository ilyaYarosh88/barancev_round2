from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.sessionFixture import SessionHelper
from fixture.groupFixture import GroupHelper
from fixture.contactFixture import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.sessionFixture = SessionHelper(self)  #помощник получает сслыкy на объекта класса application
        self.groupFixture = GroupHelper(self)
        self.contactFixture = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()