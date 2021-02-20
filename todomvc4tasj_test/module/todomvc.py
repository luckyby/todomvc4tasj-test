from selene.support.conditions import have, be
from selene.support.shared import browser
from selene.core import command


todo_all = browser.all('#todo-list>li')


def visit():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(
        True,
        "return $._data($('#clear-completed')[0], 'events')"
            ".hasOwnProperty('click')"
        "&& "
        "Object.keys(require.s.contexts._.defined).length === 39"))


def add(*todos: str):
    for todo in todos:
        browser.element('#new-todo').type(todo).press_enter()


def should_be(*todos: str):
    todo_all.should(have.exact_texts(*todos))


def todo_editing(todo: str, todo_new: str):
    todo_all.element_by(have.exact_text(todo)).double_click()
    return todo_all.element_by(have.css_class('editing')).element('.edit').perform(command.js.set_value(todo_new))


def edit(todo, todo_new):
    todo_editing(todo, todo_new).press_enter()


def toggle(todo):
    todo_all.element_by(have.exact_text(todo)).element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def delete(todo):
    todo_all.element_by(have.exact_text(todo)).hover()\
        .element('.destroy').click()


def cancel_editing(todo, todo_new):
    todo_editing(todo, todo_new).press_escape()


