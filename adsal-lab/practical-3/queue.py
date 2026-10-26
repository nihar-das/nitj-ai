class Queue:
    def __init__(self, queue_size):
        self.front = -1
        self.rear = -1
        self.queue_size = queue_size
        self.queue = [None] * queue_size

    def is_full(self):
        return self.rear == self.queue_size - 1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def enqueue(self, value):
        if self.is_full():
            print("Queue overflow")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear += 1

        self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return

        value = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1

        return value


def select_option():
    try:
        operation = input(
            "[1]:Enqueue\n[2]:Dequeue\n[3]:Exit\nSelect operation:"
        ).strip()

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


def take_queue_size():
    try:
        size = input("Enter queue size:").strip()

        if not size:
            return None
        size = int(size)

    except ValueError:
        return None

    return size


def main():
    size = take_queue_size()

    if (size is None) or (size <= 0):
        print("Invalid queue size")
        return

    queue = Queue(size)

    while True:
        # operation selection
        operation = select_option()

        # queue operations
        if operation == 1:
            # value input
            num = take_value()

            if num is None:
                print("Invalid value")
                continue

            queue.enqueue(num)
        elif operation == 2:
            val = queue.dequeue()
            if val is not None:
                print(val)
        elif operation == 3:
            break
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
