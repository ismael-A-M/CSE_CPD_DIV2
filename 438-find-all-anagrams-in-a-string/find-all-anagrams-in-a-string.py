class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=[]
        h=sorted(p)
        for i in range(len(s)-len(p)+1):
            if sorted(s[i:i+len(p)]) == h:
                l.append(i)
        return(l)