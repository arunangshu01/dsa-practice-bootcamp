"""

Josephus Circle using Circular Linked List -

Solve the Josephus problem using a circular linked list. Implement a function that takes the number of people n and the step rate k and
returns the position of the last person standing.

Output: Last person left standing: 3

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def count_nodes(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        temp = self.head
        total_nodes = self.count_nodes()
        while total_nodes != 1:
            for _ in range(step):
                temp = temp.next
            if temp.next != self.head:
                break
            self.delete_node(temp.data)
            total_nodes -= 1
        return f"Last person left standing: {temp.data}"


if __name__ == "__main__":
    cs_linked_list = CircularLinkedList()
    cs_linked_list.append(data=10)
    cs_linked_list.append(data=20)
    cs_linked_list.append(data=30)
    cs_linked_list.append(data=40)
    cs_linked_list.append(data=50)
    cs_linked_list.append(data=60)
    result = cs_linked_list.josephus_circle(step=4)
    print(result)
