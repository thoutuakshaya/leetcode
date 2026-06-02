class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
       
        minans=[]
        for i in range(len(landStartTime)):
            for j in range (len(waterStartTime)):
                T1=landStartTime[i]+landDuration[i]
                t1=max(T1,waterStartTime[j])
                T2=t1+waterDuration[j]
                minans.append(T2)
        for i in range (len(waterStartTime)):
            for j in range(len(landStartTime)):
                z1=waterStartTime[i]+waterDuration[i]
                Z1=max(z1,landStartTime[j])
                z2=Z1+landDuration[j]
                minans.append(z2)
        return min(minans)