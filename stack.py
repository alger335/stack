class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Пусто")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Пусто")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    def BalanceCheck(self, brackets):
        stack = []

        for c in brackets:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if c != ")":
                        return False
                if current_char == '{':
                    if c != "}":
                        return False
                if current_char == '[':
                    if c != "]":
                        return False
        if stack:
            return print('Пусто')
        return True
