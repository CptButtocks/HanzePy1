from stack import Stack

stack = Stack()

for i in range(10):
    stack.push(i)
while not stack.is_empty():
    print(stack.pop(), end = " ")
