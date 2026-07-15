class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping_element = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in mapping_element:
                last_element = stack.pop() if stack else '#'
                if last_element != mapping_element[i]:
                    return False
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False