from selene.support.conditions import have
from todomvc4tasj_test.model.pages import todomvc


def test_add_with(a_active_b_completed):
    todomvc.add('c')
    todomvc.should_be('a', 'b', 'c')


def test_edit_with(a_active_b_completed):
    todomvc.edit('a', 'a*')
    todomvc.should_be('a*', 'b')

    todomvc.edit('b', 'b*')
    todomvc.should_be('a*', 'b*')

    todomvc.edit('a*', '')
    todomvc.should_be('b*')

    todomvc.edit('b*', '')
    todomvc.should_be('')


def test_cancel_editing_with(a_active_b_completed):
    todomvc.cancel_editing('a', 'a*')
    todomvc.should_be('a', 'b')

    todomvc.cancel_editing('b', 'b*')
    todomvc.should_be('a', 'b')


def test_toggle_with(a_active_b_completed):
    todomvc.toggle('a')
    todomvc.should_be_completed('a', 'b')

    todomvc.toggle('b')
    todomvc.should_be_completed('a')


def test_clear_completed_with(a_active_b_completed):
    todomvc.clear_completed()
    todomvc.should_be('a')


def test_clear_completed_with(a_completed_b_completed):
    todomvc.clear_completed()
    todomvc.should_be('')


def test_delete_with(a_active_b_completed_c_active):
    todomvc.delete('a')
    todomvc.should_be('b', 'c')

    todomvc.delete('b')
    todomvc.should_be('c')

    todomvc.edit('c', '')
    todomvc.should_be()


def test_toggle_all_with(a_active_b_completed):
    todomvc.toggle_all()
    todomvc.should_be_completed('a', 'b')

    todomvc.toggle_all()
    todomvc.should_be_completed()


def test_items_left_with(a_active_b_completed):
    todomvc.items_left().should(have.exact_text('1'))

    todomvc.add('c')
    todomvc.items_left().should(have.exact_text('2'))

    todomvc.toggle_all()
    todomvc.items_left().should(have.exact_text('0'))

    todomvc.toggle_all()
    todomvc.items_left().should(have.exact_text('3'))

    todomvc.toggle('a')
    todomvc.items_left().should(have.exact_text('2'))

    todomvc.delete('b')
    todomvc.items_left().should(have.exact_text('1'))

    todomvc.clear_completed()
    todomvc.items_left().should(have.exact_text('1'))



