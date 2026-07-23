class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle = 0
        square = 0
        for i in students:
            if i==0:
                circle+=1
            else:
                square+=1
        for i in sandwiches:
            if i==0 and circle!=0:
                circle-=1
            elif i==1 and square!=0:
                square-=1
            else:
                break
        return circle + square