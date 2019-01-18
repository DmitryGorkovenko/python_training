from selenium.webdriver.firefox.webdriver import WebDriver
from addressbook_web_tests.fixture.contact import ContactHelper
from addressbook_web_tests.fixture.group import GroupHelper
from addressbook_web_tests.fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def destroy(self):
        self.wd.quit()
