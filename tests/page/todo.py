from selene.support.conditions import have
from selene.support.shared import browser


def open_todomvc4tasj():
    browser.open('https://todomvc4tasj.herokuapp.com/')


def add(text):
    browser.should(have.js_returned(True,
                     "return $._data($('#clear-completed').get(0), 'events')"
                        ".hasOwnProperty('click')"))
    browser.element('#new-todo').type(text).press_enter()


def todos():
    return browser.all('#todo-list>li')


# def have_exactly(*texts):
#     todos().should(have.exact_texts(*texts))


def complete(text):
    todos().element_by(have.exact_text(text)).element('.toggle').click()


# def clear_completed():
#     browser.element('#clear-completed').click()


def editing(text):
    def add(text):
        return editing().type(text).press_enter()

    return todos().element_by(have.exact_text(text)).double_click()


def start_editing():
    return browser.element('#todo-list').element('.editing').element('.edit')


def add_to_editing(text):
    return start_editing().type(text).press_enter()
    # todo.complete("b*")


def escape_editing():
    start_editing().type('*').press_escape()


def delete(text):
    todos().element_by(have.exact_text(text)).hover()\
        .element('.destroy').click()
