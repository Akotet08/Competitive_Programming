class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mxele = n
        lst = []
        for i in range(n-1, 0, -1):
            for k in range(mxele):
                if arr[k] == mxele:
                    self.reverse(arr, k)
                    self.reverse(arr, i)

                    print(k, mxele)
                    mxele -= 1

                    lst.append(k + 1)
                    lst.append(i+1)

                    break
        return lst
    
    def reverse(self, arr, idx):
        mid = (idx + 1) // 2
        for i in range(mid):
            arr[i], arr[idx - i] = arr[idx - i], arr[i]
        print(idx, arr)




        
                




        