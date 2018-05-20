class Stack:

    # Creates an empty stack.
    def __init__(self):
        self._theItems = list()

    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in the stack.
    def __len__(self):
        return len(self._theItems)

    # Returns the top item on the stack without removing it.
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]

    # Removes and returns the top item on the stack.
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()

    # Push an item onto the top of the stack.
    def push(self, item):
        self._theItems.append(item)

    def stack_to_que(self):
        queue = Queue()
        return [queue.enqueue(self._theItems[elem]) \
                for elem in range(0, len(self._theItems))]


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def que_to_stack(self):
        stack = Stack()
        return [stack.push(self.queue[elem]) \
                for elem in range(0, len(self.queue))]
