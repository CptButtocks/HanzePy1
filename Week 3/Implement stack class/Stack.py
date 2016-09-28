class Stack:
    def __init__(self):
        self.elements = []

    def Stack(self):
        self.elements = [];

    def is_empty(self):
        if len(self.elements) > 0:
            return False;

    def peek(self):
        return self.elements[-1];

    def push(self, value):
        self.elements.append(value);

    def pop(self):
        if len(self.elements) > 0:
            result = self.elements[-1];
            del self.elements[-1];
            return result;
        elif:
            return None;

    def getSize(self):
        return len(self.elements);
