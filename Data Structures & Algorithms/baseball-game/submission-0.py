class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        record_sum = 0
        for i in operations:
            if i == '+':
                prev_2_sum = stack[-1]+stack[-2]
                stack.append(prev_2_sum)
                record_sum+=prev_2_sum
            elif i=='D':
                temp_var = stack[-1]*2
                stack.append(temp_var)
                record_sum+=temp_var
            elif i=='C':
                record_sum-=stack[-1]
                stack.pop()
            else:
                temp_var = int(i)
                stack.append(temp_var)
                record_sum +=temp_var
        return record_sum
        
