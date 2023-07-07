from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        #split string into words
        s = s.split(" ")

        new_str = ""

        #loop through all words
        #add word to stack
        #reverse word
        #store to new variable
        for i in range(len(s)):

            #stack of word one by one
            stack = deque(s[i])

            #reverse the word
            data = "".join(stack.pop() for i in range(len(stack)))

            #add space
            data += " "

            #store reverse word 
            new_str += data
            
        #remove last added space
        new_str = new_str[:-1]  
        return new_str
    
                          
            
        


        
            
        
        
