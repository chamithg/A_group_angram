import collections
import string
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        out = collections.defaultdict(list)
        final = []
        for each in strs:
            out[("".join(sorted(each)))].append(each)
            
            
        for key,value in out.items():
            final.append(value)
        
        return final
        
        
        


obj = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(obj.groupAnagrams(strs))