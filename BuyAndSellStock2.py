import sys
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_value = sys.maxsize
        total_profit = 0
        for i in range(len(prices)):
            # Set min value
            if prices[i] <= min_value:
                min_value = prices[i]
            # if next value is bigger, substract values and add to total
            elif prices[i] > prices[i-1]:
                total_profit = total_profit + (prices[i] - prices[i-1])
                # if the next value is bigger than current, set current to min_value
                if i + 1 < len(prices)and prices[i+1] > prices[i]:
                    min_value = prices[i]
                else:
                    min_value = sys.maxsize
            # Otherwise reset min_value
            else:
                min_value = sys.maxsize
        return total_profit


if __name__ == "__main__":
    prices = [2,2,5]
    print(Solution().max_profit(prices))
