# -*- coding: utf-8 -*-
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # Эту фунцию нужно вызывать в setUp
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").submit()

    def logout(self):
        # Эту функцию нужно вызвать в TearDown
        self.app.wd.find_element_by_link_text("Logout").click()
