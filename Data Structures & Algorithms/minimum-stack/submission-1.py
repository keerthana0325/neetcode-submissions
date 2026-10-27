class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack=[]
        

    def push(self, val: int) -> None:
        p=self.stack.append(val)
        if len(self.minstack)==0:
            self.minstack.append(val)
        elif val<=self.minstack[-1]:
            self.minstack.append(val)
        return p

    def pop(self) -> None:
        dele = self.stack[-1]
        self.stack.pop()
        if dele==self.minstack[-1]:
            self.minstack.pop()
        return dele
        
            
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        # .??????????
        # if len(self.minstack)==0:
        #     self.minstack.push(..what should i push ?? ik stack but this is confusing)


        # how should i access? i mean ..? should i write a condition?
        
