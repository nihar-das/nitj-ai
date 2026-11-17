class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = [[] for _ in range(vertex_count)]

    def add_edge(self, first, second):
        if second not in self.adj_list[first]:
            self.adj_list[first].append(second)

        if first not in self.adj_list[second]:
            self.adj_list[second].append(first)

    def traverse(self, start):
        visited = [False] * self.vertex_count
        queue = [start]
        front = 0
        visited[start] = True

        while front < len(queue):
            vertex = queue[front]
            front += 1
            print(vertex, end=" ")

            for neighbour in self.adj_list[vertex]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
        print()


def select_option():
    try:
        operation = input(
            "[1]:Add edge\n[2]:Traverse\n[3]:Exit\nSelect operation:"
        ).strip()

        if not operation:
            return None
        operation = int(operation)

    except ValueError:
        return None

    return operation


def take_graph_size():
    try:
        size = input("Enter vertex count:").strip()

        if not size:
            return None
        size = int(size)

    except ValueError:
        return None

    return size


def take_vertex(vertex_count, prompt="Enter vertex:"):
    try:
        vertex = input(prompt).strip()

        if not vertex:
            return None
        vertex = int(vertex)

    except ValueError:
        return None

    if (vertex < 0) or (vertex >= vertex_count):
        return None

    return vertex


def main():
    size = take_graph_size()

    if (size is None) or (size <= 0):
        print("Invalid vertex count")
        return

    graph = Graph(size)
    print(f"Vertices: 0 to {size - 1}")

    while True:
        # operation selection
        operation = select_option()

        # graph operations
        if operation == 1:
            first = take_vertex(size, "Enter first vertex:")

            if first is None:
                print("Invalid vertex")
                continue

            second = take_vertex(size, "Enter second vertex:")

            if second is None:
                print("Invalid vertex")
                continue

            graph.add_edge(first, second)
        elif operation == 2:
            start = take_vertex(size, "Enter starting vertex:")

            if start is None:
                print("Invalid vertex")
                continue

            graph.traverse(start)
        elif operation == 3:
            break
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
