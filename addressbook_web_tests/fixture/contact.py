# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from definitions import ROOT_DIR
from pathlib import Path


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
        self.app.type("firstname", contact.first_name)
        self.app.type("middlename", contact.middle_name)
        self.app.type("lastname", contact.last_name)
        self.app.type("nickname", contact.nickname)
        self.attach(contact.file_name)
        self.app.type("title", contact.title)
        self.app.type("company", contact.company)
        self.app.type("address", contact.address)
        self.app.type("home", contact.home_phone)
        self.app.type("mobile", contact.mobile_phone)
        self.app.type("work", contact.work_phone)
        self.app.type("fax", contact.fax)
        self.app.type("email", contact.email)
        self.app.type("email2", contact.email2)
        self.app.type("email3", contact.email3)
        self.app.type("homepage", contact.homepage)
        self.fill_date(contact.bdate, day_locator="bday", month_locator="bmonth", year_locator="byear")
        self.fill_date(contact.adate, day_locator="aday", month_locator="amonth", year_locator="ayear")
        self.app.type("address2", contact.address2)
        self.app.type("phone2", contact.home_phone2)
        self.app.type("notes", contact.notes)

    def fill_date(self, date, day_locator, month_locator, year_locator):
        self.select_day(day_locator, date.day)
        self.select_month(month_locator, date.month)
        self.app.type(year_locator, date.year)

    def attach(self, file_name):
        path = ROOT_DIR + "\\addressbook_web_tests\\resources\\" + file_name
        if Path(path).is_file():
            self.app.wd.find_element_by_name("photo").send_keys(path)

    def select_day(self, locator, value):
        wd = self.app.wd
        if value:
            existing_value = wd.find_element_by_xpath("//select[@name='" + locator + "']/option[@selected='selected']")\
                .get_attribute("value")
            if value != existing_value:
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
