# Node class to store data and the next node reference
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

# LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(data)

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next_node
        return None

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count