from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.addedBack = SortedSet()
        self.currNum = 1
        

    def popSmallest(self) -> int:
        # if there are numbers in addedBack, they must be smaller than currNum
        if len(self.addedBack):
            ans = self.addedBack[0]
            self.addedBack.discard(ans)
        else:
            ans = self.currNum
            self.currNum += 1

        return ans            
        

    def addBack(self, num: int) -> None:
        if num < self.currNum and not num in self.addedBack:
            self.addedBack.add(num)

        