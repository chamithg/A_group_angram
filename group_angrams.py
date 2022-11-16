class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        strs.sort()
        output =[]
        
        j = 0
        while j < len(strs)-1:
            if not output:
                output.append([strs[j]])
                j+=1
            for i,item in enumerate(output):
                print(i , item[0], strs[j])
                if sorted(item[0]) == sorted(strs[j]) :
                    item.append(strs[j])
                    j+=1
                else:
                    if i == len(output)-1 or output == []:
                        output.append([strs[j]])
                        j+=1
                            
            
        return output  
        
        
        


obj = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(obj.groupAnagrams(strs))