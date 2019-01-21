# -*- coding: utf-8 -*-
from pathlib import Path
from selenium.webdriver.support.ui import Select

from definitions import ROOT_DIR


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def fill_contact_form(self, contact):
        fields_map = {
            'firstname': 'first_name',
            ...
        }
        for k, v in fields_map.items():
            self.app.type(k, getattr(contact, v))
        self.attach(contact.file_name)
        self.fill_date(contact.bdate, day_locator="bday", month_locator="bmonth", year_locator="byear")
        self.fill_date(contact.adate, day_locator="aday", month_locator="amonth", year_locator="ayear")

    def fill_date(self, date, day_locator, month_locator, year_locator):
        self.select_day(day_locator, date.day)
        self.select_month(month_locator, date.month)
        self.app.type(year_locator, date.year)

    def attach(self, file_name):
        path = "{}\\addressbook_web_tests\\resources\\{}".format(ROOT_DIR, file_name)
        if Path(path).is_file():
            self.app.wd.find_element_by_name("photo").send_keys(path)

    def select_day(self, locator, value):
        wd = self.app.wd
        if value:
            existing_value = wd.find_element_by_xpath("//select[@name='{}']/option[@selected='selected']".format(locator))\
                .get_attribute("value")
            if not value == existing_value:
                wd.find_element_by_name(locator).click()
                Select(wd.find_element_by_name(locator)).select_by_visible_text(value)

    def select_month(self, locator, value):
        wd = self.app.wd
        if value:
            wd.find_element_by_name(locator).click()
            Select(wd.find_element_by_name(locator)).select_by_visible_text(value)

    def return_home_page(self):
        self.app.wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.app.wd.switch_to_alert().accept()

    def modify_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_home_page()
