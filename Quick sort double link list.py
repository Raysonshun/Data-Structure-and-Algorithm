# 定义双链表

class Node:
    
   def __init__(self, val):
      self.val = val
      self.next = None
      self.prev = None
 
def dllist(arr):
    
    dummy = Node(-1)
    cur = dummy
    
    for i in arr:
        add = Node(i)
        cur.next = add
        add.pre=cur
        cur = cur.next
        
    return dummy.next, cur
      
    

def partition(start, end):
    
    if start == end:
        return
    
    key = start.val
    
    while start != end:
        
        while start != end and end.val >= key:
            end = end.pre
            
        start.val = end.val 
    
        while start != end and start.val <= key:
            start = start.next
        
        end.val = start.val 
        
    start.val = key
    
    return start

def quicksort(start,end):
    
    if start == None or start == end:
        return
    
    part = partition(start,end)
    
    if part != start:
        
        quicksort(start, part.pre)
        
    if part != end:
        
        quicksort(part.next,end)
        

arr = [1,3,6,2,10,100,7]
start, end = dllist(arr)
quicksort(start,end)


while(start):
    print(start.val)
    start = start.next
        