import heapq
class SmallestInfiniteSet:

    def __init__(self):

        self.heap=[]
        self.current=1
        self.added=set()
    def popSmallest(self) -> int:
        if self.heap:
            k=heapq.heappop(self.heap)
            self.added.remove(k)
            return k
        num=self.current
        self.current+=1
        return num
    def addBack(self, num: int) -> None:
        if num not in self.added and num<self.current:
            heapq.heappush(self.heap,num)
            self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)