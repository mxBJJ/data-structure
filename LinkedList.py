# LinkedList

''' 
         head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
'''

from time import time
from xml.etree.ElementTree import tostring


class Node:

    ## Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    ## Constructor to create an empty linked list, from head
    def __init__(self):
        self.head = None

    ## Add a new node from head
    def append(self, data):
        ## Create new Node with data
        newNode = Node(data)

        ## If head is None the list is empty and then a new node is set as head
        if self.head == None:
            self.head = newNode
            return
        
        ## If the linked list isn't empty we start from the head
        currentNode = self.head
    
        ## Travel the linked list nodes until the last node
        while currentNode.next:
            currentNode = currentNode.next

        ## Set the current node as the new node created. The node is "inserted" at end of the list
        currentNode.next = newNode
        return

    # Returns the length of the linked list.
    def length(self):
        if self.head == None:
            return 0
        currentNode = self.head
        total = 0 # Init count
        # Loop while end of linked list is not reached 
        while currentNode:
            total += 1
            currentNode = currentNode.next
        return total

    def display(self): 
        element = self.head 
        # If the list is empty, head is None
        if element is None:
            print("List has no elements")
        while element: 
            print(element.data)
            element = element.next

            if element is not None:
                print("Has next? {}".format(element.next is not None))
                print("--------------------------")
            else:
                print("next is None.")

    def to_list(self):

        # Init as empty list
        nodeData = []
        currentNode = self.head

        while currentNode:
            nodeData.append(currentNode.data)
            currentNode = currentNode.next
        return nodeData
    # Returns the value of the node at 'index'.  
    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        current_idx  = 0
        currentNode = self.head
        while currentNode != None:
            if current_idx == index: 
                return currentNode.data
            currentNode  = currentNode.next
            current_idx += 1
    # reverse a linked list
    def reverse_linkedlist(self):
        previous_node = None
        currentNode = self.head
        while currentNode != None:
            next = currentNode.next
            currentNode.next = previous_node
            previous_node = currentNode
            currentNode = next
        self.head = previous_node
    
    # Searching for an element is quite similar to counting or traversing a linked list
    def search_item(self, value):
        if self.head == None:
            print("List has no elements")
            return
        currentNode = self.head
        while currentNode != None:
            if currentNode.data == value:
                print("Item found")
                return True
            currentNode = currentNode.next
        print("Item not found")
        return False

    # Deleting an element or item from the start
    def remove_at_start(self):
        if self.head == None:
            print("The list has no element to delete")
            return 
        self.head = self.head.next
    
    # Deleting an element or item at the end
    def remove_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        currentNode = self.head
        while currentNode.next.next != None:
            currentNode = currentNode.next
        currentNode.next = None

    # This remove a node with the specified value
    def remove_element_by_value(self, value):
        # Store head node  
        currentNode = self.head  
  
        # If head node itself holds the value to be deleted  
        if currentNode != None:  
            if currentNode.data == value:  
                self.head = currentNode.next
                currentNode = None
                return
  
        # Search for the value to be deleted, keep track of the  
        # previous node as we need to change 'prev.next'  
        while currentNode != None:  
            if currentNode.data == value:  
                break
            prev = currentNode  
            currentNode = currentNode.next
  
        # if value was not present in linked list  
        if currentNode == None:  
            return
  
        prev.next = currentNode.next
        currentNode = None
    
    # add an item at the start of the list
    def insert_at_start(self, data):
        newNode        = Node(data)
        newNode.next   = self.head
        self.head = newNode

    # add an item at the end of the list   
    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode

    # add an item at any index of the list
    def insert_at_index (self, index, data):
        if index == 1:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        i = 1
        currentNode = self.head
        while i < index-1 and currentNode is not None:
            currentNode = currentNode.next
            i = i + 1
        if currentNode is None:
            print("ERROR: Index out of range!")
        else: 
            newNode = Node(data)
            newNode.next = currentNode.next 
            currentNode.next  = newNode

list = LinkedList()

list.append(5)
list.append(6)
list.append(9)
list.append(1)
list.display()

print("============================================")

list.insert_at_end(20)
list.display()

print("============================================")

list.insert_at_start(10)
list.display()

print("============================================")


print("Size: {}".format(list.length()))