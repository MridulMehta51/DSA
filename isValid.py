class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        bckt={")":"(","}":"{","]":"["}

        for i in s:
            if i in bckt:
                if stack and stack[-1]==bckt[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False 
