class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=float('inf')
        for i in strs:
            if len(i)<l:
                l=len(i)
        strg=strs[0]
        c=0
        h=""
        for i in range(len(strg)):
            if i==l:
                break
            for z in range(len(strs)):
                if i>=len(strs[z]):
                    break
                if strs[z][i]!=strg[i]:
                    c=1
            if c==0:
                h+=strg[i]
            else:
                break
        return(h)

                