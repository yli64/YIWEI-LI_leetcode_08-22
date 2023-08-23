class MinStack:

    def __init__(self):
        self.st=[] #stack
        self.min=None #min element

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.st.append(val)
            self.min=val
        else:
            if val>=self.min:
                self.st.append(val)
            else:
                self.st.append(2*val-self.min)
                self.min=val
                
    def pop(self) -> None:
        x=self.st.pop() 
        if x<self.min:
            self.min=2*self.min-x
    
    def top(self) -> int:
        x=self.st[-1]
        if x>=self.min:
            return x
        return self.min

    def getMin(self) -> int:
        return self.min