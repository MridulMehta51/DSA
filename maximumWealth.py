class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        n=0
        for i in range(len(accounts)):
            m=0
            for j in range(len(accounts[0])): 
                m+=accounts[i][j]
                
            n=max(m,n)
        return (n)

