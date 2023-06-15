#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        minIdx = i
        minEle = arr[i]
        for i in range(i + 1, len(arr)):
            if minEle > arr[i]:
                minEle = arr[i]
                minIdx = i
        return minIdx
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n - 1):
            minIdx = Solution().select(arr, i)
            if arr[minIdx] < arr[i]:
                arr[minIdx], arr[i] = arr[i], arr[minIdx]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
