class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in ds:
                ds[s[i]] += 1
            else:
                ds[s[i]] = 1
            if t[i] in dt:
                dt[t[i]] += 1
            else:
                dt[t[i]] = 1
        if dt == ds:
            print(f"{dt} == {ds}")
            return True
        else:
            print(f"{dt} != {ds}")
            return False
        