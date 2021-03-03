from selene.support.shared import browser as shared_browser
from selene.support.conditions import have, be
from selene.core import command


class ToDoMVC:


    def __init__(self, browser = shared_browser):
        self.browser = browser
        self.todo_all = browser.all("#todo-list>li")

    def todo_editing(self):
        return self.browser\
            .element('#todo-list').element('.editing').element('.edit')

    def visit(self):
        self.browser.open('https://todomvc4tasj.herokuapp.com/')

    def add(self, *todos: str):
        for todo in todos:
            self.browser\
                .should(have.js_returned(True,
                    "return  $._data($('#clear-completed').get(0), 'events')"
                        ".hasOwnProperty('click') "
                    "&& "
                    "Object.keys(require.s.contexts._.defined).length === 39"))
            self.browser.element('#new-todo').type(todo).press_enter()

    def should_be(self, *todos: str):
        if todos is None or todos == ('',):
            self.todo_all.should(have.size(0))
        else:
            self.todo_all.should(have.exact_texts(*todos))

    def should_be_completed(self, *todos):
        if todos is None or todos == ('',):
            for todo in self.todo_all:
                todo.should(have.css_class('active'))
        else:
            self.browser.element('#todo-list').all('.completed')\
                .should(have.exact_texts(*todos))

    def edit(self, todo: str, todo_new: str):
        self.todo_all.element_by(have.exact_text(todo)).should(be.clickable)
        self.todo_all.element_by(have.exact_text(todo)).double_click()
        self.todo_editing().perform(command.js.set_value(todo_new))\
            .press_enter()

    def toggle(self, todo: str):
        self.todo_all.element_by(have.exact_text(todo)).element('.toggle')\
            .should(be.clickable)
        self.todo_all.element_by(have.exact_text(todo)).element('.toggle')\
            .click()

    def clear_completed(self):
        self.browser.element('#clear-completed').should(be.clickable)
        self.browser.element('#clear-completed').click()

    def delete(self, todo: str):
        self.todo_all.element_by(have.exact_text(todo)).hover() \
            .element('.destroy').click()

    def cancel_editing(self, todo: str, todo_new: str):
        self.todo_all.element_by(have.exact_text(todo)).double_click()
        self.todo_editing().perform(command.js.set_value(todo_new))\
            .press_escape()

    def toggle_all(self):
        self.browser.element('#toggle-all').should(be.clickable)
        self.browser.element('#toggle-all').click()

    def items_left(self):
        return self.browser.element('#todo-count strong')

