# -*- coding: utf-8 -*-
from addressbook_web_tests.model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="123", header=None, footer=""))
    app.session.logout()
