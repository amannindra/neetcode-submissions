class Solution:
    def isValid(self, s: str) -> bool:
        print(f"Start: {len(s)}")
        stack = []
    
        for i in range(len(s)):
            if len(stack) > 0:
                print(f"{s[i]} == {stack[-1]}")
                if s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                elif s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop()   
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        print(stack)
        if len(stack) > 0:
            return False
        return True