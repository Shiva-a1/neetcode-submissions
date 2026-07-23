from collections import deque
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = deque(sandwiches)
        students_preferences = Counter(students)
        while sandwiches:
            ss = sandwiches[0]
            if students_preferences[ss]:
                sandwiches.popleft()
                students_preferences[ss]-=1
            else:
                break
        return len(sandwiches)