class Stack:
 
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else: 
            return False


    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        if not self.isEmpty():
            en_stack = enumerate(self.items)
            for index, value in en_stack:
                if (index == len(self.items) - 1):
                    print(value, end = "\n")
                else:
                    print(value, end = ", ")
            