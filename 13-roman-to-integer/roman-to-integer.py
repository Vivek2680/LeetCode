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
            current = roman_dict[s[index]]
            if index + 1 < len(s) and current < roman_dict[s[index + 1]]:
                result -= current
            else:
                result += current

        return result
obj = Solution()
print(obj.romanToInt('XXX'))