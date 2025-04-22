#'''
from collections import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
q.appendleft(5)
q.extend([40,50,60])
q.rotate(1)
q.rotate(-1)
print(q)   # deque([10, 20, 30])
print(q.pop()) # last deleted 30
print(q.popleft()) # 10
print()

'''
q.appendleft(5)  # Adds 5 to the left end
q.extend([40, 50])  # Extends deque with multiple elements from the right
q.extendleft([2, 1])  # Extends deque with multiple elements from the left (added in reverse order)
q.rotate(1)  # Rotates elements one step to the right
q.rotate(-1)  # Rotates elements one step to the left

'''

class Node:
    """A Node of a Singly Linked List"""
    def __init__(self, data):
        self.data = data  # Store value
        self.next = None  # Pointer to the next node
class SLL:        
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning"""
        '''
        new_node = Node(data)
        new_node.next = self.head  # Link new node to the previous head
        self.head = new_node  # Update head to the new node  
        '''
#--------2nd way-- 
         
        new_node = Node(data)
        if not self.head:
           self.head = new_node
           return
        temp = self.head
        print("head", end=" -> ") #execute 1 time only
        while temp.next: 
            
           temp = temp.next
        temp.next = new_node
#-------------        
    def display(self):
        temp= self.head
        while temp:
           print(temp.data, end= " -> ")
           temp=temp.next
        print("None")   

s= SLL()
s.insert_at_beginning(1)
s.insert_at_beginning(2)
s.display()
#Output
#head -> 1 -> 2 -> None
'''
class NodeDLL:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node= Node(data)
        new_node.next= self.head
        self.head=new_node
        new_node.prev=
    def display2(self):
        

dll= DLL() 
dll.insert_at_beginning(3)
dll.insert_at_beginning(5) 
dll.display1()      
'''        


        
        
        
        
        
        
        
        
        
        
        
        