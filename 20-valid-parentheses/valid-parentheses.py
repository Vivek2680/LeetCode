class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }
        my_list = []
        for ch in s:
            # if  ch in parentheses_dict.values():
            #     my_list.append(ch)
            # elif ch in parentheses_dict:
            #     if not my_list:
            #         return False
            #     else:
            #         if my_list[-1] == parentheses_dict[ch]:
            #             my_list.pop()
            #         else:
            #             return False
            if ch in parentheses_dict:
                if not my_list or my_list[-1] != parentheses_dict[ch]:
                    return False
                my_list.pop()
            else:
                my_list.append(ch)
            
        return not my_list
        
obj = Solution()
print(obj.isValid('()'))