class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.list.pop()

    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        return "Stack is empty!"

    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)


s = Stack()

print("Is empty?", s.is_empty())      # ก่อน push ยังว่างอยู่

# push ค่า 1–5
for i in range(1, 6):
    s.push(i)

print("Size after push:", s.size())
print("Top element:", s.peek())

# pop ออกทีละอัน
for _ in range(5):
    print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())
