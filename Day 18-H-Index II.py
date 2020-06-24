class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt=0
        for c in range(len(citations)-1,-1,-1):
            cnt+=1
            if citations[c]<cnt:
                return cnt-1
        return cnt
            
            
      
