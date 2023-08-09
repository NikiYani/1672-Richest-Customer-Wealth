class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = -1
        sum = 0
        
        for i in range(0, len(accounts)) :
            for j in range(0, len(accounts[i])) :
                sum += accounts[i][j]
            
            if max > sum :
                max = max
            else :
                max = sum
            sum = 0
        
        return max