class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        recSum = 0
        total = 0



        for i in range(len(operations)):
            if operations[i] == '+':
                recSum = record[-1] + record[-2]
                record.append(recSum)
            elif operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                prod = 2*record[-1]
                record.append(prod)
            else:
                record.append(int(operations[i]))
        total = sum(record)
        return total

        