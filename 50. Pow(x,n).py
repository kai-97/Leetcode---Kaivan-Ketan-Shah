class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1

        positive = 0 if n<0 else 1
        power = n if positive else -1*n

        def recursion(result, powe):
            if powe == 0:
                return 1
            if powe%2==0:
                num = recursion(result, powe//2)
                return num*num
            return x*recursion(result, powe-1)

        return recursion(x,power) if positive else 1/recursion(x,power)