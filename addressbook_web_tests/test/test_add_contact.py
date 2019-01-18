# -*- coding: utf-8 -*-
from addressbook_web_tests.fixture.application import Application
from addressbook_web_tests.model.contact import Contact
from addressbook_web_tests.model.date import Date
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="abc", middle_name="abc", last_name="abc", nickname="abc",
                               title="abc", company="abc", address="abc", home_phone="abc", mobile_phone="abc",
                               work_phone="abc", fax="abc", email="abc", email2="abc", email3="abc",
                               homepage="abc", bdate=Date("1", "January", "1990"),
                               adate=Date("10", "May", "1999"), address2="abc", home_phone2="abc",
                               notes="abc", file_name="photo.jpg"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="",
                               address="", home_phone="", mobile_phone="", work_phone="", fax="", email="",
                               email2="", email3="", homepage="", bdate=Date(None, None, ""),
                               adate=Date(None, None, ""), address2="", home_phone2="", notes="", file_name=""))
    app.logout()
