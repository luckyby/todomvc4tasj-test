from todomvc4tasj_test.model import todomvc


def test_add():
    todomvc.visit()
    todomvc.should_be_items_left(0)

    todomvc.add('a')

    todomvc.should_be('a')
    todomvc.should_be_items_left(1)

    todomvc.add('b', 'c')

    todomvc.should_be('a', 'b', 'c')
    todomvc.should_be_items_left(3)

    todomvc.toggle('b')
    todomvc.should_be_items_left(2)

    todomvc.add('')

    todomvc.should_be('a', 'b', 'c')
    todomvc.should_be_items_left(2)


def test_edit():
    todomvc.visit_with_a_active_b_completed()

    todomvc.edit('a', 'a*')

    todomvc.should_be('a*', 'b')
    todomvc.should_be_items_left(1)

    todomvc.edit('b', 'b*')

    todomvc.should_be('a*', 'b*')
    todomvc.should_be_items_left(1)

    todomvc.edit('a*', '')

    todomvc.should_be('b*')
    todomvc.should_be_items_left(0)

    todomvc.edit('b*', '')

    todomvc.should_be('')
    todomvc.should_be_items_left(0)

def test_cancel_editing():
    todomvc.visit_with_a_active_b_completed()
    todomvc.should_be_items_left(1)

    todomvc.cancel_editing('a', 'a*')

    todomvc.should_be('a', 'b')

    todomvc.cancel_editing('b', 'b*')

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(1)


def test_activate():
    todomvc.visit_with_a_active_b_completed()

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(1)

    todomvc.toggle('b')

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(2)


def test_complete():
    todomvc.visit_with_a_active_b_completed()

    todomvc.toggle('a')

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(0)


def test_clear_completed():
    todomvc.visit_with_a_active_b_completed()

    todomvc.clear_completed()

    todomvc.should_be('a')

    todomvc.toggle('a')
    todomvc.clear_completed()

    todomvc.should_be('')


def test_delete():
    todomvc.visit_with_a_active_b_completed()

    todomvc.delete('a')

    todomvc.should_be('b')

    todomvc.delete('b')

    todomvc.should_be()


def test_activate_all():
    todomvc.visit_with_a_active_b_completed()
    todomvc.toggle('a')

    todomvc.should_be_items_left(0)

    todomvc.toggle_all()

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(2)


def test_complete_all():
    todomvc.visit()
    todomvc.add('a', 'b')
    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(2)

    todomvc.toggle_all()

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(0)

    todomvc.toggle('a')

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(1)

    todomvc.toggle_all()

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(0)
