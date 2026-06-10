class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_dict ={
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for index in range(len(s)):
            if index < len(s)-1 and roman_dict[s[index]] < roman_dict[s[index + 1]]:
                result -= roman_dict[s[index]]
            else:
                result += roman_dict[s[index]]
        return result
obj = Solution()
print(obj.romanToInt('XXX'))