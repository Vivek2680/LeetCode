class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)

        return num == num[ : :-1]
obj = Solution()
print(obj.isPalindrome(212))