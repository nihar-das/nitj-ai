class Stack:
    def __init__(self, stack_size):
        self.top = -1
        self.stack_size = stack_size
        self.stack = [None] * stack_size

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return
        value = self.stack[self.top]
        self.top -= 1
        return value

    def is_full(self):
        return self.top == self.stack_size - 1

    def is_empty(self):
        return self.top == -1


def select_option():
    try:
        operation = input("[1]:Push\n[2]:Pop\n[3]:Exit\nSelect operation:").strip()

        if not operation:
            return None
        operation = int(operation)

    except ValueError:
        return None

    return operation


def take_value():
    try:
        num = input("Enter value:").strip()

        if not num:
            return None
        num = float(num)

    except ValueError:
        return None

    return num


def take_stack_size():
    try:
        size = input("Enter stack size:").strip()

        if not size:
            return None
        size = int(size)

    except ValueError:
        return None

    return size


def main():
    size = take_stack_size()

    if (size is None) or (size <= 0):
        print("Invalid stack size")
        return

    stack = Stack(size)

    while True:
        # operation selection
        operation = select_option()

        # stack operations
        if operation == 1:
            # value input
            num = take_value()

            if num is None:
                print("Invalid value")
                continue

            stack.push(num)
        elif operation == 2:
            val = stack.pop()
            if val is not None:
                print(val)
        elif operation == 3:
            break
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
