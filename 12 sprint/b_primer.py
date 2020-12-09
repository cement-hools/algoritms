class Node:  
    def __init__(self, value, next=None):  
        self.value = value  
        self.next = next  
    
    def __repr__(self):  
        return self.value
    
    def __str__(self):  
        return str(self.value)
        
def hasCycle(head):
    a, b = head, head
    while a and a.next:
        a = a.next.next 
        b = b.next
        if a is b:
            return True
    return False

so = Node(7,)   
sa = Node(6, so)   
fr = Node(5, sa)   
th = Node(4, fr)           
we = Node(3, th)   
tu = Node(2, we)   
mo = Node(1, tu)        
so.next = mo
def solution(x):
    print(x.value)
    while x.next is not None:
        x = x.next
        print(x.value)
    return x.next

# solution(mo)
print(hasCycle(mo))
