from selene.support.shared import browser
from selene import have, be

def test_e2e_task_management():

    browser.open( 'https://todomvc4tasj.herokuapp.com/')

    browser.should(have.js_returned(True,
            "return $._data($('#clear-completed').get(0), 'events')"
            ".hasOwnProperty('click')"))
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('#todo-list li').element_by(have.exact_text('b')).double_click()
    browser.element('#todo-list').element('.editing').element('.edit')\
        .type('*').press_enter()

    browser.all('#todo-list li ').element_by(have.exact_text('b*'))\
        .element('.toggle').click()
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))

    browser.all('#todo-list li').element_by(have.exact_text('a'))\
        .double_click()
    browser.element('#todo-list').element('.editing').element('.edit')\
        .type('*').press_escape()

    browser.all('#todo-list li').element_by(have.exact_text('a')).hover()\
        .element('.destroy').click()
    browser.all('#todo-list>li').should(have.exact_texts('c'))
