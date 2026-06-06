class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        # arr=[]
        # for i in range( len(temperatures)):
        #     count=0
        #     find=False
        #     for j in range (i+1,len(temperatures)):
        #         if(temperatures[i]<temperatures[j]):
        #             arr.append(j-i)
                    
        #             find=True
        #             break
                
        #     if (find==False): 
        #         arr.append(0)
        # return arr

        # ans=[]*len*(len(temperatures))
        # for i in range(len(temperatures)):
        #     while stack and temperatures[i] > temperatures[stack[-1]]:
        #         idx = stack.pop()
        #         ans[idx] = i - idx
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans