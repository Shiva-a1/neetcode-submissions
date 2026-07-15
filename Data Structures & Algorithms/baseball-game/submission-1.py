class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        record_sum = 0
        for i in operations:
            if i == '+':
                stack.append(stack[-1]+stack[-2])
                record_sum+=stack[-1]
            elif i=='D':
                stack.append(stack[-1]*2)
                record_sum+=stack[-1]
            elif i=='C':
                record_sum-=stack[-1]
                stack.pop()
            else:
                stack.append(int(i))
                record_sum +=stack[-1]
        return record_sum
        
