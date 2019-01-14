# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact
from date import Date
import os


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def create_contact(self, wd, contact):
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        self.upload_photo(wd, contact.file_name)
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
        self.fill_date(wd, contact.bdate, day_locator="bday", month_locator="bmonth", year_locator="byear")
        self.fill_date(wd, contact.adate, day_locator="aday", month_locator="amonth", year_locator="ayear")
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.home_phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").submit()

    def fill_date(self, wd, date, day_locator, month_locator, year_locator):
        if len(date.day) > 0 and len(date.month) > 0:
            wd.find_element_by_name(day_locator).click()
            Select(wd.find_element_by_name(day_locator)).select_by_visible_text(date.day)
            wd.find_element_by_name(month_locator).click()
            Select(wd.find_element_by_name(month_locator)).select_by_visible_text(date.month)
        wd.find_element_by_name(year_locator).send_keys(date.year)

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def upload_photo(self, wd, file_name):
        if len(file_name) > 0:
            wd.find_element_by_name("photo").click()
            wd.find_element_by_name("photo").send_keys(os.getcwd() + "/" + file_name)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(first_name="abc", middle_name="abc", last_name="abc", nickname="abc",
                                        title="abc", company="abc", address="abc", home_phone="abc", mobile_phone="abc",
                                        work_phone="abc", fax="abc", email="abc", email2="abc", email3="abc",
                                        homepage="abc", bdate=Date("1", "January", "1990"),
                                        adate=Date("10", "May", "1999"), address2="abc", home_phone2="abc",
                                        notes="abc", file_name="photo.png"))
        self.return_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="",
                                        address="", home_phone="", mobile_phone="", work_phone="", fax="", email="",
                                        email2="", email3="", homepage="", bdate=Date("", "", ""),
                                        adate=Date("", "", ""), address2="", home_phone2="", notes="", file_name=""))

        self.return_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
