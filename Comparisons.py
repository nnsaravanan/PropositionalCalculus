class Variable:
    '''function to create a variable that can either be true or false'''
    def __init__(self, char,value = True):
        self.char = char
        self.value = value

    def __str__(self):
        return str(self.char)
    def __repr__(self):
        return str(self.char)
     
    def __bool__(self):
        return self.value
    
    
class Constant(Variable):
    '''constant to create values that are always true'''
    def __init__(self,left):
        self.left = left
        if self.left.value!=None:
            self.value = self.eval()

    def eval(self):
        return bool(self.left)
    
    def __str__(self):
        return f"{self.left}"
    def __repr__(self):
        return f"{self.left}"
    
    def __bool__(self):
        return self.value

class Negation(Variable):
    '''negation to create a negation of a variable'''
    def __init__(self,left):
        self.left = left
        if self.left.value!=None:
            self.value = self.eval()

    def eval(self):
        return not(bool(self.left))
    
    def __str__(self):
        return f"~{self.left}"
    def __repr__(self):
        return f"~{self.left}"
    
    def __bool__(self):
        return self.value

class Conjunction(Variable):
    '''conjunction to check whether 2 variables are true'''
    def __init__(self,left,right):
        self.left = left
        self.right = right
        if self.left.value != None != self.right.value:
            self.value = self.eval()

    def eval(self):
        return bool(self.left) and bool(self.right)
    
    def __str__(self):
        return f"({self.left} ^ {self.right})"
    def __repr__(self):
        return f"({self.left} ^ {self.right})"
    
    def __bool__(self):
        return self.value

class Disjunction(Variable):
    '''disjunction to check whether 1 of 2 variables are true'''
    def __init__(self,left,right):
        self.left = left
        self.right = right
        if self.left.value != None != self.right.value:
            self.value = self.eval()

    def eval(self):
        return bool(self.left) or bool(self.right)
    
    def __str__(self):
        return f"({self.left} v {self.right})"
    def __repr__(self):
        return f"({self.left} v {self.right})"
    
    def __bool__(self):
        return self.value

class Conditional(Variable):
    '''conditional to check whether 1 variable leads to another'''
    def __init__(self,left,right):
        self.left = left
        self.right = right 
        if self.left.value != None != self.right.value:
            self.value = self.eval()  

    def eval(self):
        return not bool(self.left) or (bool(self.left) and bool(self.right))
    
    def __str__(self):
        return f"({self.left} -> {self.right})"
    def __repr__(self):
        return f"({self.left} -> {self.right})"
    
    def __bool__(self):
        return self.value

class Biconditional(Variable):
    '''biconditional to check if 2 variables are equal'''
    def __init__(self,left,right):
        self.left = left
        self.right = right
        if self.left.value != None != self.right.value:
            self.value = self.eval()

    def eval(self):
        return bool(self.left) == bool(self.right)
    
    def __str__(self):
        return f"({self.left} v {self.right})"
    def __repr__(self):
        return f"({self.left} v {self.right})"
    
    def __bool__(self):
        return self.value
            
