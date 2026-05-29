class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''''
        My reasoning:
        I could check letter for to see if they appear in either string, but this does not scale to larger strings.
        I could sort it alphabetically and try to see if they then match, also does not scale well.
        Then there is the dictionary approach that would save the count of each letter in a dict. This would scale well.
        '''''
        if len(s) != len(t):  
            return False  
        else:
            s_dict = dict()  
            t_dict = dict()  
            
        for letter in s:
            if letter not in s_dict:  
                s_dict[letter] = 1  
            else:
                s_dict[letter] +=1  
        
        for letter in t:  
            if letter not in t_dict:  
                t_dict[letter] = 1  
            else:  
                t_dict[letter] +=1  
        
        if t_dict == s_dict:
            return True  
        else: 
            return False
        
            
        