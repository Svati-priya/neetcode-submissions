class Solution(object):
    def sumOfSqaureOfDigits(self, n):
        sum = 0
        # 36 -> % 10 -> 6 -> square of 6 -> 36 -> now we have to extract 3 so we will do:-> 36 // 10 -> 3 -> 3 % 10 -> 0
        # dig -> 6 now when we get 3 we will do n % 10 and then sqaure this 3 which will be 9 
        # sum = 36 and then add that 9 -> 45
        while n > 0:
            dig = n % 10
            sum = sum + (dig * dig)
            n = n // 10
        return sum 

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # slow, fast = n
        # function  who returns sum of sqaure of digits
        slow = n 
        fast = n
        while fast != 1:
            slow = self.sumOfSqaureOfDigits(slow)
            fast = self.sumOfSqaureOfDigits(self.sumOfSqaureOfDigits(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
        return True