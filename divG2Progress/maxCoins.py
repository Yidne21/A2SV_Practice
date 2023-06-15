class Solution:

    def maxCoins(self, piles):
        piles.sort()
        n = len(piles) - 2
        ite = 0
        maxCoin = 0
        while(ite < len(piles) // 3):
            maxCoin += piles[n]
            n -= 2
            ite += 1
        return maxCoin
