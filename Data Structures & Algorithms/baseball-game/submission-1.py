class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit():
                l.append(int(operations[i]))
            elif operations[i] == "+":
                l.append(l[-1] + l[-2])
            elif operations[i] == 'D':
                l.append(2 * l[-1])
            elif operations[i] == 'C':
                l.pop()
        return sum(l)
