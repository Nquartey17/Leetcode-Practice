import sys
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_price = 0
        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            elif prices[i] - min_value > max_price:
                max_price = prices[i] - min_value
        return max_price


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().max_profit(prices))


