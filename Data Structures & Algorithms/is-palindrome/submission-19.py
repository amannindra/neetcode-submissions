class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1
        print(f"j: {j}")
        
        if len(s) == 0 or len(s) == 1:
            return True

        while i <= j:
            if s[i].isalnum() == False:
                i += 1
                continue
            if s[j].isalnum() == False:
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                print(f"{s[i]} != {s[j]}, [{i}, {j}]")
                return False
            else:
                i += 1
                j -= 1


        # while i <= j:
        #     while  and s[i].isalnum() == False:
        #         i += 1
        #     while s[j] and s[j].isalnum() == False:
        #         j -= 1

        #     if s[i].lower() != s[j].lower():
        #         print(f"{s[i]} != {s[j]}")
        #         return False
        #     else:
        #         i += 1
        #         j -= 1
            

        return True