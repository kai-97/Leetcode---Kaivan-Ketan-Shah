class Solution:
    def trailingZeroes(self, n: int) -> int:

        # Logic - factor or 5 and 2 together will make a 10, which adds a zero to the number.
        # Usually there are more factors of 2 compared to factors of 5 for a number range.
        # therefore, if we simply find the number of factors of 5 for that number, we shall get
        # the number of trailing zeroes.
        counter = 0
        while n>0:
            # floor divide the number by 5 till we get to 0
            n = n//5
            counter += n
        return counter