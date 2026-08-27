class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 1
        highest = 1
        if len(s) < 1:
            return 0        
        sub = s[0]
        while L < len(s) - 1 and R < len(s):
            # self.subSection(s, L, R)
            if s[R] in sub:
                sub = sub[1:]
                L += 1
            else:
                sub += s[R]
                R += 1
 
            if len(sub) > highest:
                print(f'highest = {len(sub)}')
                highest = len(sub)
        return highest
        