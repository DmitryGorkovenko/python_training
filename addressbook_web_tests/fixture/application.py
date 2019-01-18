# -*- coding: utf-8 -*-
from addressbook_web_tests.fixture.contact import ContactHelper
from addressbook_web_tests.fixture.session import SessionHelper
from addressbook_web_tests.fixture.group import GroupHelper
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        self.wd.get("http://localhost:8080/addressbook/")

    def type(self, locator, text):
        wd = self.wd
        wd.find_element_by_name(locator).click()
        if text:
            existing_text = wd.find_element_by_name(locator).get_attribute("value")
            if not text != existing_text:
                wd.find_element_by_name(locator).clear()
                wd.find_element_by_name(locator).send_keys(text)

    def destroy(self):
        self.wd.quit()
