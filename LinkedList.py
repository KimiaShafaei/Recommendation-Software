from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get_head(self):
        return self.head
    
    def add_to_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        
    def show_list(self):
        current = self.head
        while current:
            print(current.value, end = "->")
            current = current.next