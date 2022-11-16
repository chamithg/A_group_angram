class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # strs.sort()
        output =[]
        
        for each in strs:
            
            x = len(output)
            i = 0
            while i < x  or x ==0:
                if not output:
                    output.append(each)
                    i +=1
                else:
                    print(i)
                    if "".join(sorted(each))== sorted(output[i][0]):
                        output[i].append(each)
                        i +=1
                    if "".join(sorted(each))!= sorted(output[i][0]) and i == len(output)-1:
                        output.append(each)
                        i +=1
                
                x = len(output)   
            
            
            
        return output  
        
        
        


obj = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(obj.groupAnagrams(strs))