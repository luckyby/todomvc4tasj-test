from selene.support.shared import browser as shared_browser
from selene.support.conditions import have
from selene.core import command


class ToDoMVC:

    def __init__(self, browser = shared_browser):
        self.browser = browser
        self.todo_all = browser.all("#todo-list>li")

    def start_editing(self, todo: str, todo_new: str):
        self.todo_all.element_by(have.exact_text(todo)).double_click()
        return self.todo_all.element_by(have.css_class('editing'))\
            .element('.edit').perform(command.js.set_value(todo_new))

    def visit(self):
        self.browser.open('https://todomvc4tasj.herokuapp.com/')
        self.browser \
            .should(have.js_returned(
                True,
                 "return  $._data($('#clear-completed').get(0), 'events')"
                        ".hasOwnProperty('click') "
                 "&& "
                 "Object.keys(require.s.contexts._.defined).length === 39")
            )

    def visit_with(self, *todos: str):
        self.visit()
        self.add(*todos)

    def add(self, *todos: str):
        for todo in todos:
            self.browser.element('#new-todo').type(todo).press_enter()

    def delete(self, todo: str):
        self.todo_all.element_by(have.exact_text(todo)).hover() \
            .element('.destroy').click()

    def edit(self, todo: str, todo_new: str):
        self.start_editing(todo, todo_new).press_enter()

    def edit_with_press_tab(self, todo: str, todo_new: str):
        self.start_editing(todo, todo_new).press_tab()

    def cancel_editing(self, todo: str, todo_new: str):
        self.start_editing(todo, todo_new).press_escape()

    def toggle(self, todo: str):
        self.todo_all.element_by(have.exact_text(todo)).element('.toggle')\
            .click()

    def toggle_all(self):
        self.browser.element('#toggle-all').click()

    def clear_completed(self):
        self.browser.element('#clear-completed').click()

    def should_be(self, *todos: str):
        self.todo_all.should(have.exact_texts(*todos))

    def should_be_active(self, *todos):
        self.todo_all.filtered_by(have.css_class('active'))\
            .should(have.exact_texts(*todos))

    def should_be_completed(self, *todos):
        self.todo_all.filtered_by(have.css_class('completed'))\
            .should(have.exact_texts(*todos))

    def should_be_items_left(self, count):
        self.browser.element('#todo-count strong')\
                .should(have.exact_text(f'{count}'))

    def should_be_empty(self):
        self.todo_all.should(have.size(0))
