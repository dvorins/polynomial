class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        repr_p1 = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Div, Mul)) else repr(self.p1)
        repr_p2 = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Div, Mul)) else repr(self.p2)
        
        return repr_p1 + " + " + repr_p2

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        repr_p1 = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Div, Mul)) else repr(self.p1)
        repr_p2 = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Div, Mul)) else repr(self.p2)
        
        return repr_p1 + " * " + repr_p2

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        repr_p1 = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Div, Mul)) else repr(self.p1)
        repr_p2 = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Div, Mul)) else repr(self.p2)
        
        return repr_p1 + " / " + repr_p2

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        repr_p1 = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Div, Mul)) else repr(self.p1)
        repr_p2 = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Div, Mul)) else repr(self.p2)
        
        return repr_p1 + " - " + repr_p2



poly1 = Add(Int(2), Mul(X(), Int(3))) # should be 2 + (X * 3)
print(poly1, "\n")
 
poly2 = Sub(Mul(X(), Int(5)), Div(Int(10), X()))
print(poly2, "\n") 

poly3 = Add(Add(Int(2), Mul(X(), Int(3))), Sub(Mul(X(), X()), Div(X(), Int(2))))
print(poly3, "\n") 