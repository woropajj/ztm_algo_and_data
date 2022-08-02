# 10 -> 5 -> 16

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):  # __str__ tu nie zadzialalo
        return str(self.__dict__)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def print_list(self):
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next

        return array

    def __str__(self):
        return "LinkedList: " + str(self.__dict__)

    def insert(self, index, value):
        # check params
        if index >= self.length:
            self.append(value)
            return print(self.print_list())

        new_node = Node(value)
        leader = self.traverse_to_index(index - 1)
        holding_pointer = leader.next
        leader.next = new_node
        new_node.next = holding_pointer
        self.length += 1
        return print(self.print_list())

    def remove(self, index):
        assert index >= 0, "index should be non negative you dummy!"
        if index > self.length:
            print("You can't remove stuff that isn't there!")
            return

        if index == 0:
            self.head = self.traverse_to_index(index + 1)
        else:
            leader = self.traverse_to_index(index - 1)
            unwanted_node = leader.next
            leader.next = unwanted_node.next
        self.length -= 1

        return print(self.print_list())

    def traverse_to_value(self, value):
        current_node = self.head
        while value != current_node.value:
            current_node = current_node.next

        return current_node

    def traverse_to_index(self, index):
        # check params
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1

        return current_node


myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
# print(myLinkedList.print_list())
# myLinkedList.insert(2, 99)
# myLinkedList.insert(20, 88)
# myLinkedList.remove(5)
# myLinkedList.remove(0)
# myLinkedList.remove(100)
print(myLinkedList)
