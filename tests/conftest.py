import json
import pytest
from selene.support.shared import browser


def local_storage_set(local_storage_value):
    browser.open('https://todomvc4tasj.herokuapp.com/')
    local_storage_value_dumped = json.dumps(local_storage_value)
    browser.driver.execute_script("window.localStorage.setItem("
            "'todos-troopjs', "
            "arguments[0]);", local_storage_value_dumped)
    browser.driver.refresh()


@pytest.fixture()
def a_active_b_active():
    local_storage_value = [{"completed": False, "title": "a"},
                            {"completed": False,"title":"b"}]
    local_storage_set(local_storage_value)

    yield

    browser.driver.execute_script("localStorage.clear()")


@pytest.fixture()
def a_active_b_completed():
    local_storage_value = [{"completed": False, "title": "a"},
                            {"completed": True, "title": "b"}]
    local_storage_set(local_storage_value)

    yield

    browser.driver.execute_script("localStorage.clear()")


@pytest.fixture()
def a_active_b_completed_c_active():
    local_storage_value = [{"completed": False, "title": "a"},
                          {"completed": True, "title": "b"},
                          {"completed": False, "title": "c"}]
    local_storage_set(local_storage_value)

    yield

    browser.driver.execute_script("localStorage.clear()")