class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def swap(self, n1, n2):
        if n1 == n2:
            print("Nodes are the same, there is no swap needed")
            return

        prevNode1 = None
        prevNode2 = None
        node1 = self.head
        node2 = self.head

    
        while node1 and node1.data != n1:
            prevNode1 = node1
            node1 = node1.next

        while node2 and node2.data != n2:
            prevNode2 = node2
            node2 = node2.next

        if not node1 or not node2:
            print("Node1, Node2 or both not found. SWAP NOT POSSIBLE")
            return

        if prevNode1:
            prevNode1.next = node2
        else:
            self.head = node2

        if prevNode2:
            prevNode2.next = node1
        else:
            self.head = node1

        node1.next, node2.next = node2.next, node1.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next
        print("None")


def main():
    l = SinglyLL()

    num = int(input("Enter the number of nodes: "))
    print("Enter node values:")
    for _ in range(num):
        data = int(input())
        l.append(data)

    print("\nOriginal Linked List:")
    l.display()

    n1 = int(input("\nEnter first node to swap: "))
    n2 = int(input("Enter second node to swap: "))

    l.swap(n1, n2)

    print("\nLinked List after swapping:")
    l.display()

if __name__ == "__main__":
    main()
