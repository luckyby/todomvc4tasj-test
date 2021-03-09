from todomvc4tasj_test.model import todomvc


def test_add_with_empty_todos():
    todomvc.visit_with('')

    todomvc.add('a')

    todomvc.should_be('a')
    todomvc.should_be_items_left(1)


def test_add_several_todos():
    todomvc.visit_with('a')

    todomvc.add('b', 'c')

    todomvc.should_be('a', 'b', 'c')
    todomvc.should_be_items_left(3)


def test_add_empty_todo():
    todomvc.visit_with('a')

    todomvc.add('')

    todomvc.should_be('a')
    todomvc.should_be_items_left(1)


def test_edit():
    todomvc.visit_with('a', 'b')

    todomvc.edit('a', 'a*')

    todomvc.should_be('a*', 'b')
    todomvc.should_be_items_left(2)


def test_edit_to_empty():
    todomvc.visit_with('a', 'b')

    todomvc.edit('a', '')

    todomvc.should_be('b')
    todomvc.should_be_items_left(1)


def test_edit_with_out_of_focus():
    todomvc.visit_with('a', 'b')

    todomvc.edit_with_press_tab('a', 'a*')

    todomvc.should_be('a*', 'b')
    todomvc.should_be_items_left(2)


def test_cancel_editing():
    todomvc.visit_with('a', 'b')

    todomvc.cancel_editing('a', 'a*')

    todomvc.should_be('a', 'b')
    todomvc.should_be_items_left(2)


def test_activate():
    todomvc.visit_with_completed('a', 'b')

    todomvc.toggle('a')

    todomvc.should_be('a', 'b')
    todomvc.should_be_active('a')
    todomvc.should_be_items_left(1)


def test_complete():
    todomvc.visit_with('a', 'b')

    todomvc.toggle('a')

    todomvc.should_be('a', 'b')
    todomvc.should_be_completed('a')
    todomvc.should_be_items_left(1)


def test_clear_completed():
    todomvc.visit_with_completed('a', 'b')

    todomvc.clear_completed()

    todomvc.should_be_empty()


def test_delete_one_of_several():
    todomvc.visit_with('a', 'b', 'c')

    todomvc.delete('b')

    todomvc.should_be('a','c')
    todomvc.should_be_items_left(2)


def test_delete_one_to_empty():
    todomvc.visit_with('a')

    todomvc.delete('a')

    todomvc.should_be_empty()


def test_activate_all():
    todomvc.visit_with_completed('a', 'b')

    todomvc.toggle_all()

    todomvc.should_be('a', 'b')
    todomvc.should_be_active('a', 'b')
    todomvc.should_be_items_left(2)


def test_complete_all_active():
    todomvc.visit_with('a', 'b')

    todomvc.toggle_all()

    todomvc.should_be('a', 'b')
    todomvc.should_be_completed('a', 'b')
    todomvc.should_be_items_left(0)
