# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from pathlib import Path
import os


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        self.attach(contact.file_name)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        self.fill_date(contact.bdate, day_locator="bday", month_locator="bmonth", year_locator="byear")
        self.fill_date(contact.adate, day_locator="aday", month_locator="amonth", year_locator="ayear")
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.home_phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def fill_date(self, date, day_locator, month_locator, year_locator):
        self.select(day_locator, date.day)
        self.select(month_locator, date.month)
        self.app.wd.find_element_by_name(year_locator).send_keys(date.year)

    def attach(self, file_name):
        path = os.getcwd() + "\\addressbook_web_tests\\resources\\" + file_name
        if Path(path).is_file():
            self.app.wd.find_element_by_name("photo").send_keys(path)

    def select(self, locator, value):
        wd = self.app.wd
        if value:
            wd.find_element_by_name(locator).click()
            Select(wd.find_element_by_name(locator)).select_by_visible_text(value)

    def return_home_page(self):
        self.app.wd.find_element_by_link_text("home page").click()
