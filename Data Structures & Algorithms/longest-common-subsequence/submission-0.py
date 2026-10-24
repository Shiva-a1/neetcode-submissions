class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        prevRow = [0]* (cols+1)
        st1 = " "+text1
        st2 = " "+text2
        for i in range(1, len(st1)):
            currRow = [0]* (cols+1)
            for j in range(1, cols+1):
                if st1[i]==st2[j]:
                    currRow[j]= prevRow[j-1]+1
                else:
                    currRow[j] = max(currRow[j-1], prevRow[j])
            prevRow = currRow
        return prevRow[-1]
        