class DequeIterator:
    pointToFirst = None
    def __init__(self,deq):
        "docstring"
        self.pointToFirst = deq.first
        
    def __next__(self):
        if self.pointToFirst == None:
            raise StopIteration
        ret,self.pointToFirst = self.pointToFirst,self.pointToFirst.next 
        return ret.value
    

class Deque:
    first = None
    last = None

    def __iter__(self):
        return DequeIterator(self)
    
    def __init__(self, firstElement):
        "docstring"
        self.last = self.first = Contener()
        self.last.value = firstElement


        
    def push_first(self,elem ):
        n = Contener()
        n.value = elem
        n.next = self.first
        self.first.prev = n
        self.first = n

    def push_last(self,elem ):
        n = Contener()
        n.value = elem
        n.prev = self.last
        self.last.next = n
        self.last = n

    def pop_first():
        n = self.first
        self.first = self.first.next
        self.first.prev = None
        return n.value
    
    def pop_last():
        n = self.last
        self.last = self.last.prev
        self.last.next = None
        return n.value
    
    

    def is_palindrome(self, ):
        come_to_first = self.first
        come_to_last = self.last

        while(come_to_first != come_to_last):
            if come_to_last.value != come_to_first.value:
                return False
            come_to_last = come_to_last.prev
            come_to_last = come_to_first.next
            
        return True

    def addString(self,string_to_add ):
        for a in string_to_add:
            self.push_last(a)

    def __str__(self):
        str_to_return=''
        cur = self.first
        while cur != None:
            str_to_return += str(cur.value) + " | "
            cur = cur.next
        return str_to_return

    def remove(self,rmv_me):
        cur = self.first
        while cur != None:
            if cur.value == rmv_me:
                cur.prev.next = cur.next
                if cur.next != None:
                    cur.next.prev = cur.prev
            cur = cur.next

    def aply_a_lambda(self, lamb):
        cur = self.first
        while cur != None:
            cur.value = lamb(cur.value)
            cur = cur.next
            
class Contener:
    next = None
    prev = None
    value = None
    
if __name__ == '__main__':
    a = Deque('a')
    print(a.is_palindrome())
    a.addString(" baHH non")
    a.remove(" ")
    a.aply_a_lambda(lambda v : v.lower())
    print(a)
    for b in a:
        print(b)
