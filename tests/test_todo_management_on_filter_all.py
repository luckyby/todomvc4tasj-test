from todomvc4tasj_test.model import todomvc


def test_add_one_when_empty():
    todomvc.visit_with()
    todomvc.should_be_empty()

    todomvc.add('a')

    todomvc.should_be('a')
    todomvc.should_be_items_left(1)


def test_add_several_when_empty():
    todomvc.visit_with()
    todomvc.should_be_empty()

    todomvc.add('a','b', 'c')

    todomvc.should_be('a', 'b', 'c')
    todomvc.should_be_items_left(3)


def test_edit():
    todomvc.visit_with('a', 'b', 'c')

    todomvc.edit('b', 'b*')

    todomvc.should_be('a', 'b*', 'c')
    todomvc.should_be_items_left(3)


def test_delete_by_edit_to_empty():
    todomvc.visit_with('a', 'b', 'c')

    todomvc.edit('b', '')

    todomvc.should_be('a', 'c')
    todomvc.should_be_items_left(2)


def test_edit_by_focus_change():
    todomvc.visit_with('a', 'b', 'c')

    todomvc.edit_with_press_tab('b', 'b*')

    todomvc.should_be('a', 'b*', 'c')
    todomvc.should_be_items_left(3)


def test_cancel_editing():
    todomvc.visit_with('a', 'b', 'c')

    todomvc.cancel_editing('b', 'b*')

    todomvc.should_be('a', 'b', 'c')
    todomvc.should_be_items_left(3)


def test_activate():
    todomvc.visit_with('a', 'b', 'c')
    todomvc.toggle_all()

    todomvc.toggle('b')

    todomvc.should_be_active('b')
    todomvc.should_be_completed('a', 'c')
    todomvc.should_be_items_left(1)


def test_complete():
    todomvc.visit_with('a', 'b', 'c')

    todomvc.toggle('b')

    todomvc.should_be_completed('b')
    todomvc.should_be_active('a', 'c')
    todomvc.should_be_items_left(2)


def test_delete():
    todomvc.visit_with('a', 'b', 'c')

    todomvc.delete('b')

    todomvc.should_be('a','c')
    todomvc.should_be_items_left(2)


def test_delete_one_to_empty():
    todomvc.visit_with('a')

    todomvc.delete('a')

    todomvc.should_be_empty()

def test_clear_completed():
    todomvc.visit_with('a', 'b', 'c')
    todomvc.toggle('b')

    todomvc.clear_completed()

    todomvc.should_be_active('a', 'c')
    todomvc.should_be_completed()
    todomvc.should_be_items_left(2)

def test_complete_all():
    todomvc.visit_with('a', 'b', 'c')

    todomvc.toggle_all()

    todomvc.should_be_completed('a', 'b', 'c')
    todomvc.should_be_active()
    todomvc.should_be_items_left(0)


def test_activate_all():
    todomvc.visit_with('a', 'b', 'c')
    todomvc.toggle_all()

    todomvc.toggle_all()

    todomvc.should_be_active('a', 'b', 'c')
    todomvc.should_be_completed()
    todomvc.should_be_items_left(3)
