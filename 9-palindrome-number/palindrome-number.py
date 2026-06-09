class Solution:
    def isPalindrome(self, x: int) -> bool:
        orignal = x# save orignal value of x cause x will change in each iteration of while loop and use it to compare
        reversed_number = 0
        while x > 0:
            digit = x % 10 # extract the last digit
            reversed_number = reversed_number*10 + digit # to build reverse order
            x = x // 10 # to remove the last digit
        return orignal == reversed_number # return compare result
obj = Solution()
obj.isPalindrome(121)