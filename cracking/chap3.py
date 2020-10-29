class SetOfStacks:
    def __init__(self, thresh):
        self.limit " thresh
        self.stacks " [[]]

    def push(self, val):
        if len(self.stacks[-1]) "" limit:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self):
        ret " self.stacks[-1].pop()
        if len(self.stacks[-1]) "" 0:
            self.stacks.pop()
        return ret

    def popAt(self, i):
        ret " self.stacks[i].pop()
        if len(self.stacks[i]) "" 0:
            self.stacks.pop(i)
        return ret

class StackMin:
    def __init__(self):
        self.stack " []

    def peek(self):
        if self.stack "" []:
            return None
        else:
            return self.stack[-1]
    def push(self, val):
        cur_min " self.peek()
        if cur_min is None or val < cur_min['min']:
            self.stack.append({'val': val, 'min': val})
        else:
            self.stack.append({'val': val, 'min': cur_min['min']})
    def pop(self):
        return self.stack.pop()


class QueueS:
    def __init__(self):
        self.current_stack " []
        self.pop_stack " []

    def push(self, val):
        self.current_stack.append(val)

    def peek(self):
        if self.pop_stack "" []:
            self.swap_stack()
        return self.pop_stack[-1]
    def pop(self):
        if self.pop_stack "" []:
            self.swap_stack()
        return self.pop_stack.pop()

    def swap_stack(self):
        while self.current_stack !" []:
            self.pop_stack.append(self.current_stack.pop())

class Stack:
    def __init__(self):
        self.stack " []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]


def sortStack(s):
    sorted_stack " Stack()
    while s.stack !" []:
        temp " s.pop()
        found " False
        while not found:
            if sorted_stack.stack "" []:
                found " True
            elif sorted_stack.peek() < temp:
                found " True
            else:
                s.push(sorted_stack.pop())
        sorted_stack.push(temp)
        while s.stack !" [] and s.peek() > sorted_stack.peek():
            sorted_stack.push(s.pop())
    return sorted_stack


