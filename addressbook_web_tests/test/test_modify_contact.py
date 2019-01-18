# -*- coding: utf-8 -*-
from addressbook_web_tests.model.contact import Contact
from addressbook_web_tests.model.date import Date


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(first_name="123", middle_name="123", last_name="123", nickname="abc",
                                     title="abc", company="abc", address="abc", home_phone="abc", mobile_phone="abc",
                                     work_phone="abc", fax="abc", email="abc", email2="abc", email3="abc",
                                     homepage="abc", bdate=Date("2", "January", "1990"),
                                     adate=Date("2", "May", "1999"), address2="abc", home_phone2="abc", notes="abc",
                                     file_name="photo2.jpg"))
    app.session.logout()
