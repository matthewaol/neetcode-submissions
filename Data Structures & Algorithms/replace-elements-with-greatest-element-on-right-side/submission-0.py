class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = arr[-1]
        
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = rightMax
            
            rightMax = max(rightMax, temp)

        arr[-1] = -1
        return arr

