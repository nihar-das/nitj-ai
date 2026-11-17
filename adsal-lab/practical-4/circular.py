class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            node.next = self.head
            return

        current = self.head
        while current.next is not self.head:
            current = current.next

        current.next = node
        node.next = self.head

    def delete(self, key):
        if self.head is None:
            print("List empty")
            return

        if self.head.value == key:
            value = self.head.value

            if self.head.next is self.head:
                self.head = None
            else:
                current = self.head
                while current.next is not self.head:
                    current = current.next

                self.head = self.head.next
                current.next = self.head

            return value

        current = self.head
        while current.next is not self.head:
            if current.next.value == key:
                value = current.next.value
                current.next = current.next.next
                return value

            current = current.next

        print("Key not found")

    def traverse(self):
        if self.head is None:
            print("List empty")
            return

        current = self.head
        while True:
            print(current.value, end=" ")
            current = current.next
            if current is self.head:
                break
        print()


def select_option():
    try:
        operation = input(
            "[1]:Create\n[2]:Insert\n[3]:Delete\n[4]:Traverse\n[5]:Exit\nSelect operation:"
        ).strip()

        if not operation:
            return None
        operation = int(operation)

    except ValueError:
        return None

    return operation


def take_value(prompt="Enter value:"):
    try:
        num = input(prompt).strip()

        if not num:
            return None
        num = float(num)

    except ValueError:
        return None

    return num


def main():
    linked_list = None

    while True:
        # operation selection
        operation = select_option()

        # linked list operations
        if operation == 1:
            linked_list = CircularLinkedList()
        elif (operation in (2, 3, 4)) and (linked_list is None):
            print("List not created")
        elif operation == 2:
            # value input
            num = take_value()

            if num is None:
                print("Invalid value")
                continue

            linked_list.insert(num)
        elif operation == 3:
            # key input
            key = take_value("Enter key:")

            if key is None:
                print("Invalid key")
                continue

            val = linked_list.delete(key)
            if val is not None:
                print(val)
        elif operation == 4:
            linked_list.traverse()
        elif operation == 5:
            break
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
