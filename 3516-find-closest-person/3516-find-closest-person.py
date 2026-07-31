class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        ans = 0
        p1 = abs(abs(z) - abs(x))
        p2 = abs(abs(z) - abs(y))
        if p1 < p2:
            ans = 1
        elif p2 == p1:
            ans = 0
        else:
            ans = 2
        return ans
