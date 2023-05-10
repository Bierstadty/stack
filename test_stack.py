"""tests for Stack class"""
from random import randint
from stack import Stack


def test_size():
    """Check if Stack.size() works correctly."""

    stack = Stack()
    assert stack.size() == 0
    number = randint(1, 10)
    for i in range(number):
        stack.push(i)
    assert stack.size() == number


def test_is_empty():
    """Check if Stack.is_empty() works correctly."""

    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()


def test_top():
    """Check if Stack.top() works correctly."""

    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    stack.pop()
    assert stack.top() == 1


def test_pop():
    """Check if Stack.pop() works correctly."""

    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.top() == 1


def test_push():
    """Check if Stack.push(elem) works correctly."""

    stack = Stack()
    stack.push(1)
    assert stack.top() == 1
    number = randint(1, 10)
    for i in range(number):
        stack.push(i)
    assert stack.size() == number + 1
    assert stack.top() == number - 1


def test_data():
    """Check if Stack.size() works correctly."""

    stack = Stack()
    for i in range(5):
        stack.push(i)
    assert stack.data() == [0, 1, 2, 3, 4]
