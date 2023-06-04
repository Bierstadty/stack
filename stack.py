"""
    Implementation of Stack.
"""


class Stack:
    """
        Class that has functionality of a stack.

        Methods
        -------
        is_empty()
            Reply if the stack is empty.

        size()
            Return the amount of the stack's elements.

        top()
            Return the topmost element from the stack.

        pop()
            Deletes the topmost element of the stack.

        push(element=int)
            Add the element to the top of the stack.

        data()
            Return the current version of the stack as a list.
    """

    def __init__(self):
        """
            Init SampleClass.
        """
        self._data = []

    def size(self) -> int:
        """
            Return the amount of the stack's elements.
        """
        return len(self._data)

    def is_empty(self) -> bool:
        """
            Reply if the stack is empty.
        """
        return len(self._data) == 0

    def top(self) -> int:
        """
            Return the topmost element from the stack.
        """
        if not self.is_empty():
            return self._data[-1]
        raise IndexError("No such as element. Stack is empty")

    def pop(self) -> int:
        """
            Delete and return the topmost element of the stack.
        """
        if not self.is_empty():
            removed_elem = self._data[-1]
            del self._data[-1]
            return removed_elem
        raise IndexError('Stack is empty.')

    def push(self, element: int) -> None:
        """
            Add the element to the top of the stack.
        """
        self._data.append(element)

    def __repr__(self) -> str:
        """
            Represent a class’s objects as a string.
        """
        return "Stack" + "(" + str(self._data)[1:-1] + ")"

    def data(self) -> list:
        """
            Return the current version of the stack as a list.
        """
        return self._data
