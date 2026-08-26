class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        # if len(s) == 2:
        #     if s[0].isalpha() and s[1].isalpha():
        #         if s[0].lower() == s[1].lower():
        #             return True
        #         else:
        #             return False
        #     else:
        #         return False

        while i < j:
            if not s[i].isalnum():
                i += 1   
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            print(f"Comparing {s[i]} and {s[j]} at {i} and {j}")
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

                
            




        # print("j", j)


        # isi = ""
        # jsj = ""
        # for i in range(int(len(s)/2)):
        #     if s[i].isalpha():
        #         isi += s[i].lower()
        # print(int(len(s)/2))
         
        # r = 0  
        # for j in range(int(len(s)/2)):
        #     if s[len(s) - 1 - j].isalpha():

        #         jsj += s[len(s) - 1 - j].lower()
        #     r+= 1
        
        # print(r)


        # print(isi)
        # print(jsj)        


        # while i != j:
        #     if s[i].isalpha() and s[j].isalpha():
        #         if s[i] != s[j]:
        #             print(f"Returning false because {s[i]} != {s[j]} at i = {i}, j = {j}")
        #             return False
        #     i += 1
        #     j -= 1
        # return true


        