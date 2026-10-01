class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisValid = False
        stack = [ ]
        pairs = { ")":"(", "]" : "[", "}" : "{" }

        for parenthes in s:
            if parenthes in "([{":
                stack.append(parenthes)
            elif not stack or stack.pop() != pairs[parenthes]:
                return False
        if len(stack) == 0:
            parenthesisValid = True
        
        return parenthesisValid