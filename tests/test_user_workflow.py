from todomvc4tasj_test.model import todomvc

def test_main_management():

    todomvc.visit_with()

    todomvc.add('a', 'b', 'c')
    todomvc.should_have('a', 'b', 'c')

    todomvc.edit('b', 'b*')

    todomvc.toggle('b*')
    todomvc.clear_completed()
    todomvc.should_have('a', 'c')

    todomvc.cancel_editing('a', 'a*')

    todomvc.delete('a')
    todomvc.should_have('c')
