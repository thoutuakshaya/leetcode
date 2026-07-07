class Solution:
    def sumAndMultiply(self, n: int) -> int:
        arr=[]
        for i in str(n):
            if i!='0':
                arr.append(int(i))
        if not arr:
            return 0
        s=sum(arr)
        k=int("".join(str(i) for i in arr))
        return k*s