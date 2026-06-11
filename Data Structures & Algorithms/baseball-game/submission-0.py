class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == 'D':
                record.append(int(record[-1]) * 2)
            elif op == 'C':
                record.pop()
            elif op == '+':
                record.append(int(record[-1] + record[-2]))
            else:
                record.append(int(op))
        sum = 0
        print(record)
        for r in record:
            sum += r
        return sum
