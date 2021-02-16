from selene.support.conditions import have
from selene.support.shared import browser
from tests.page.todo import todos


def have_exactly(*texts):
    todos().should(have.exact_texts(*texts))

def clear_completed():
    browser.element('#clear-completed').click()
