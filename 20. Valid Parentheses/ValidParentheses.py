class Solution:
    
    def isValid(self, s: str) -> bool:        
        stack = []
        charMaps = {')':'(', ']':'[', '}':'{'}        
        for char in s:            
            if char in charMaps.values():
                stack.append(char)                
            if char in charMaps:
                if len(stack)!=0 and stack[-1]==charMaps.get(char):
                    stack.pop()
                else:                    
                    return False                
        if len(stack)==0:
            return True
        return False