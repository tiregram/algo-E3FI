from math import sin


class Circular_vector:
    "cette class est un circular vector"
    
    buffer_tab = []
    vector_size = 0
    vector_first = 0
    vector_last = 0

    
    def __init__(self, sizeBuffer,fisrtElement = 0):
        "docstring"
        self.buffer_tab = [None]*sizeBuffer
        self.buffer_tab[0] = 0
        
        self.vector_size = 1
        
        self.vector_first = 0
        self.vector_last = 0

        
    def insert_last(self,element):
        if(self.vector_size == len(self.buffer_tab)):
            print("buffer is out of range to insert"+str(element)) 
            return False
        
        self.vector_last = self.get_next_indice(self.vector_last)
        self.buffer_tab[self.vector_last] = element
        self.vector_size +=1
        return True
   
        

    def insert_first(self,element):
        if(self.vector_size == len(self.buffer_tab)):
            print("buffer is out of range to insert"+str(element) )
            return False

        self.vector_first = self.get_previous_indice(self.vector_first);
        self.buffer_tab[self.vector_first] = element
        self.vector_size += 1
        return True
            
   
    def remove_last(self):
        return not self.pop_last() == None
        

    def remove_first(self):
        return not self.pop_first() == None

    def pop_first(self):
        # TODO
        if self.vector_size == 0:
            return None

        
        ret = self.buffer_tab[self.vector_first]

        
        self.buffer_tab[self.vector_first] = None
        self.vector_first = self.get_next_indice(self.vector_first)
        self.vector_size -= 1
        
        return ret;
        
    def pop_last(self):
        # TODO
        if self.vector_size == 0:
            return None
        

        
        ret = self.buffer_tab[self.vector_last]
        

        self.buffer_tab[self.vector_last] = None
        self.vector_last = self.get_previous_indice(self.vector_last)
        self.vector_size -= 1
        return ret;
    
    def erase_all(self):
        while self.remove_first():
            pass
        
        
        

    def set_relatif(self):
        pass

    def __str__(self):
        ret  = "circular:\n"
        ret += "size:\t"+str(self.vector_size)+"\t"
        ret += "BeginAt:\t"+str(self.vector_first)+"\t"
        ret += "EndAt:\t"+str(self.vector_last)+"\n"
        
        for a in self.buffer_tab:
            ret =ret +str( a) +", "

        return ret
    
    def get_next_indice(self, indice):
        return (indice + 1 + len(self.buffer_tab)) % len(self.buffer_tab)

    def get_previous_indice(self,indice):
        return (indice - 1 + len(self.buffer_tab)) % len(self.buffer_tab)

    def get_tab(self):
        # TODO: recopi sur les element a partie de la fin et du debut
        if self.vector_size == 0:
            return
        
        if self.vector_first < self.vector_last:
            return self.buffer_tab[self.vector_first:self.vector_last+1]
        
        else:
            return self.buffer_tab[self.vector_first:]+self.buffer_tab[:self.vector_last+1]
            
    def augment(self,fois,plus):
        tab  = self.get_tab()
        if tab != None :
            self.vector_first = 0
            self.vector_last  = len(tab) -1
            self.vector_len   = len(tab)
        
            newSize = len(self.buffer_tab) *  fois + plus - len(tab)
            self.buffer_tab = tab + [None] * newSize

        else:
            self.vector_len  = 0
            self.vector_first = 1
            self.vector_last = 0
            
            newSize = len(self.buffer_tab) *  fois + plus 
            self.buffer_tab = [None] * newSize
            
        
        
    
    
    def shring(self,div, minus):
        # TODO: calcul de la nouvelle taille pour savoir si l'ancien tableau entre dans le nouveaux
        tab = self.get_tab()
        
        pass
    
        
if __name__ == '__main__':

    cv = Circular_vector(20)
    
    print("insert test last:")
    cv.insert_last(10)
    cv.insert_last(11)
    cv.insert_last(12)
    print(str(cv))
    
    print("insert test first:")
    cv.insert_first(9)
    cv.insert_first(8)
    cv.insert_first(7)
    print(str(cv))

    print("remove test last:")
    cv.remove_last()
    cv.remove_last()
    cv.remove_last()
    print(str(cv))

    print("remove test first:")
    cv.remove_first()
    cv.remove_first()
    cv.remove_first()
    print(str(cv))
    
    
    print("add 10 element:") 
    [cv.insert_last(a) for a in range(1,10)]
    print(str(cv))

    print("remove all:")
    cv.erase_all()
    print(str(cv))

    [cv.insert_last(a) for a in range(1,14)]
    
    print(cv)
    cv.augment(2,0)
    cv.insert_last(42)
    cv.insert_first(43)
    print(cv)
    cv.shring(1,0)
