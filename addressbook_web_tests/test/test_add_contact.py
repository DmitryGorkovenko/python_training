# -*- coding: utf-8 -*-
from addressbook_web_tests.model.contact import Contact
from addressbook_web_tests.model.date import Date

fields = ('first_name', 'middle_name', ...)


def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    data = {field_name: 'abc' for field_name in fields}
    app.contact.create(Contact(
        bdate=Date('1', 'January', '1990'), adate=Date('10', 'May', '1999'), file_name='photo.jpg',
        **data
    ))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username='admin', password='secret')
    data = {field_name: '' for field_name in fields}
    app.contact.create(Contact(
        bdate=Date(None, None, ''), adate=Date(None, None, ''),
        **data,
    ))
    app.session.logout()
