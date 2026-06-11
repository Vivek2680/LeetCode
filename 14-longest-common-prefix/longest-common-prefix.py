from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        shortest_element = min(strs, key= len)
        if not strs:
            return common

        for idx, element in enumerate(shortest_element):
            '''
            here shortest element is flow and this for loop iterate through word 'flow'
            give us f, l, o, w
            '''
            # print(element)
            for ch in strs:
                print(ch[0])
                '''
                here ch is element of list strs means flower, flow, flight
                '''
                # print(ch)
                if ch[idx] != element:
                    '''
                    it compare letter of ch upto idx of element(flow) mean 0 to 3 index of ch if they are not same as "flow"
                    then return common otherwish continue
                    '''
                    return common
                '''
                add letter which are same only 
                like flow and flower it will add f in 0th iteration then l in 1st iteration.....so on 
                '''
            common += element
        return common
obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))