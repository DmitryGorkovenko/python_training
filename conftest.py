# -*- coding: utf-8 -*-
from addressbook_web_tests.fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
