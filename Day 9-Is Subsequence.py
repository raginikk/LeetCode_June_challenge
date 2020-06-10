class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i < len(s) and j < len(t):
            i, j = i + (s[i] == t[j]), j + 1
            
        return i == len(s)

        
