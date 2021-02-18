from selene.support.conditions import have
from selene.support.shared import browser
from selene.core import command


def open():
    browser.open('https://todomvc4tasj.herokuapp.com/')


def add(*todos):
    for todo in todos:
        browser.should(have.js_returned(True,
                    "return $._data($('#clear-completed').get(0), 'events')"
                    ".hasOwnProperty('click')"))
        browser.element('#new-todo').type(todo).press_enter()


def should_be(*todos):
    todo_all().should(have.exact_texts(*todos))


def todo_all():
    return browser.all('#todo-list>li')


def todo_editing():
    return browser.element('#todo-list').element('.editing').element('.edit')


def edit(todo_old, todo_new):
    todo_all().element_by(have.exact_text(todo_old)) \
        .double_click()
    todo_editing() \
        .perform(command.js.set_value(todo_new)).press_enter()


def toggle(todo):
    todo_all().element_by(have.exact_text(todo)).element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def delete(todo):
    todo_all().element_by(have.exact_text(todo)).hover()\
        .element('.destroy').click()


def cancel_editing(todo_old, todo_new):
    todo_all().element_by(have.exact_text(todo_old)) \
        .double_click()
    todo_editing().type(todo_new).press_escape()


