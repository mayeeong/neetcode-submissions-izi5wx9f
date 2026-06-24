class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if len(cost)<=2:
            return min(cost)
        
        x = [0] * (n+1)
        
        for i in range(2, n+1):
            x[i] = min(x[i-1]+cost[i-1], x[i-2]+cost[i-2])

        return x[n]
        

            
            

