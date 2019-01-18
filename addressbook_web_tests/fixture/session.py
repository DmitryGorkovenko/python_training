# -*- coding: utf-8 -*-
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").submit()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()
        time.sleep(0.1)
        # Без этой функции time.sleep(0.1) не работают тесты в случае настройки scope="session" для фикстуры.
        # Одновременно с нажатием логаут происходит уже переход на страницу создания группы (контакта).
