class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = node
        node.prev = current

    def delete(self, key):
        if self.head is None:
            print("List empty")
            return

        current = self.head
        while current is not None:
            if current.value == key:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next

                if current.next is not None:
                    current.next.prev = current.prev

                value = current.value
                current.next = None
                current.prev = None
                return value

            current = current.next

        print("Key not found")

    def traverse(self):
        if self.head is None:
            print("List empty")
            return

        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
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
            linked_list = DoublyLinkedList()
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
