class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)//2 
        costDifference=[]
        cost = 0
        for x in costs:
            costDifference.append(x[1]-x[0])
            cost = cost+x[0]
        
        costDifference = sorted(costDifference)[:N] 
        for c in costDifference:
            cost = cost + c 
        return cost    
        
