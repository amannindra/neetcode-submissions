class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            word = 1
            for j in i:
                word *= ord(j)

            if str(word) in d:
                preb = d[str(word)] 
                print(f"Trying to add {i} to {preb} and {type(preb)} in {d}")
                preb.append(i)
                d[str(word)] = preb
            else:
                d[str(word)] = [i]
        
        output = []
        return list(d.values())
  

        


