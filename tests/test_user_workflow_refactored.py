from tests.page import todos, todo
from tests.page.todo import open_todomvc4tasj

def test_e2e_task_management():
    open_todomvc4tasj()

    todo.add('a')
    todo.add('b')
    todo.add('c')
    todos.have_exactly('a', 'b', 'c')

    todo.editing('b')
    todo.add_to_editing('*')
    todo.complete('b*')
    todos.clear_completed()
    todos.have_exactly('a', 'c')

    todo.editing('a')
    todo.escape_editing()
    todo.delete('a')
    todos.have_exactly('c')
