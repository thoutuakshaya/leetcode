class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        sum1=0
        for i in range(num1, num2+1):
            list1=[]
            list1=list(map(int,str(i)))
            for i in range (1,len(list1)-1):
                if (list1[i]<list1[i+1] and list1[i]<list1[i-1]) or (list1[i]>list1[i+1] and list1[i]>list1[i-1]) :
                    sum1=sum1+1
        return sum1