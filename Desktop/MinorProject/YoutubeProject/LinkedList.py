class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class SinglyLinkedList:        
    def __init__(self):
        self.head=None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next = new_node    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next= self.head
        self.head=new_node
        
    def delete_node(self,key):
        temp= self.head
        if temp and temp.data==key:
            self.head = temp.next
            temp=None
            return
        prev = None
        while temp and temp.data != key:
            prev =temp
            temp=temp.next
        if temp is None:
            print("Key not found")
            return
        prev.next=temp.next
        text=None
        
    def search(self,key):
        temp =self.head
        while temp:
            if temp.data==key:
                return True
            temp =temp.next
        return False    
        
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data, end=' -> ')
            temp=temp.next
        print("None")   

l1 = SinglyLinkedList()
l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.insert_at_beginning(0)
l1.traverse()
print("Search 2:", l1.search(2))#Search 2: True
l1.delete_node(2)
l1.traverse()
#__________________________________________________________
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(data):
    
    def insert_at_end(data):
    
    def delete(self,data):    
    
    def traverse(self,key):
        
    def search(self,key):    
'''
















        
        












