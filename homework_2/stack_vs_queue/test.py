from stack_queue import Stack, Queue

stack = Stack()
assert stack.is_empty() is True

stack.push(1)
stack.push(2)
stack.push(3)
assert stack.peek() == 3
assert stack.pop() == 3
assert stack.pop() == 2
assert stack.peek() == 1
assert stack.pop() == 1
assert stack.is_empty() is True

try:
    stack.pop()
    assert False
except IndexError:
    pass

try:
    stack.peek()
    assert False
except IndexError:
    pass

for i in range(100000):
    stack.push(i)
for i in range(99999, -1, -1):
    assert stack.pop() == i
assert stack.is_empty() is True

queue = Queue()
assert queue.is_empty() is True

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
assert queue.peek() == 1
assert queue.dequeue() == 1
assert queue.dequeue() == 2
assert queue.peek() == 3
assert queue.dequeue() == 3
assert queue.is_empty() is True

try:
    queue.dequeue()
    assert False
except IndexError:
    pass

try:
    queue.peek()
    assert False
except IndexError:
    pass

for i in range(100000):
    queue.enqueue(i)
for i in range(100000):
    assert queue.dequeue() == i
assert queue.is_empty() is True

queue.enqueue(10)
queue.enqueue(20)
assert queue.dequeue() == 10
queue.enqueue(30)
assert queue.dequeue() == 20
assert queue.dequeue() == 30
assert queue.is_empty() is True
