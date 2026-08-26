class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            a[tuple(count)].append(s)

        print(a.values())
        return list(a.values())
        


        

        #     # if s in l:
        #     #     l.append((word, c))
        # print(l)
        # # k = []
        # # for i in range(len(l) - 1):
        # #     p = []
        # #     for j in range(i, len(l)):
        # #         if l[i][1] == l[j][1]:
        # #             p.append(l[i][0])
        # #             p.append(l[j][0])
        # #     k.append(p)
        # # print(k)

        # [1,2,3,1,3,7,4,6]
        # [[1,1],[2], [3,3], [7], [4], [6]]

                
            
    
  

        


