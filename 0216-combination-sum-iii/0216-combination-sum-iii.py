class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result=[]
        def backtrack(start,s,nums):
            if len(nums)==k:
                if s==n:
                    result.append(nums.copy())
                return
            for i in range(start ,10):
                s+=int(i)
                nums.append(i)

                backtrack(i+1,s,nums)

                nums.pop()
                s-=int(i)
            
        backtrack(1,0,[])

        return result
