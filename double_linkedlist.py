'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail

    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=self.head
            return
        self.head.prev=new_node
        new_node.next=self.head
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.tail is None:
            self.insert_at_beginning(new_node)
            return
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

    def delete_at_beginning(self):
        self.head=self.head.next
        self.head.prev=None
    def delete_at_end(self):
        self.tail.prev.next=None
        self.tail=self.tail.prev


L=DoubleLinkedList()
L.insert_at_beginning(3)
L.insert_at_beginning(2)
L.insert_at_beginning(1)
L.insert_at_end(4)
L.delete_at_beginning()
L.delete_at_end()
L.traverse()
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=self
class CircularLinkedList:
    def __init__(self):
        self.head=None
        
    def count(self):
        c=1
        if self.head is None:
            return 0
        
        current=self.head
        while current.next is not self.head  :
            c+=1
            current=current.next
        return c
        
    def traverse(self):
        if self.head is None:
            return
        current=self.head
        if self.head.next is self.head:
            print(self.head.data)
            return
        while current.next is not self.head:
            print(current.data)
            current=current.next
        print(current.data)
    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head =new_node
            return
        new_node.next=self.head
        current=self.head
        while current.next is not self.head:
            current=current.next
        current.next=new_node
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.insert_at_beginning(data)
            return
        current=self.head
        while current.next is not self.head:
            current=current.next
        current.next=new_node
        new_node.next=self.head

L=CircularLinkedList()
L.insert_at_beginning(3)
L.insert_at_beginning(2)
L.insert_at_beginning(1)
L.insert_at_end(4)
L.insert_at_end(5)

L.traverse()
print(L.head.data)

