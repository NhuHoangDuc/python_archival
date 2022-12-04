




class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
        
    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            next_node=self.head.next
            new_node.next=self.head
            self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=new_node
    def count(self):
        c=0
        current=self.head
        while current is not None:
            c+=1
            current=current.next
        return c

    def delete_at_first(self):
        new_head=self.head.next
        self.head=new_head
    def delete_at_last(self):
        current=self.head
        while current.next.next is not None:
            current=current.next
        current.next=None
        





class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

L= LinkedList()
L.insert_at_beginning(3)
L.insert_at_beginning(2)
L.insert_at_beginning(1)
L.insert_at_end(4)
L.delete_at_first()
L.delete_at_last()
L.traverse()

node1=Node(5)
