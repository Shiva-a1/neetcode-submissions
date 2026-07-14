class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = arr[-1]
        for i in range(len(arr)-2, 0, -1):
            if arr[i] > max_element:
                arr[i], max_element = max_element, arr[i]
            else:
                arr[i] = max_element
        arr[0] = max_element
        arr[-1] = -1
        return arr