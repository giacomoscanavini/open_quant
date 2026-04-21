"""
Buy and Sell Stock
You are given an array of stock prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.
Write a python program that will return the maximum profit 
you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

import numpy as np
from typing import List

def buy_and_sell_stock(prices: List[int]) -> int:
    """
    Code includes a nested loop 
    Time complexity analysis:
        Outer loop --> O(n)
        Inner loop --> O(n)
        Total complexity --> O(n^2)

    Space complexity analysis:
        We are only defining a handful of variables --> O(1)
    """
    max_profit = 0

    for i in range(len(prices)):
        j = len(prices) - 1

        while j > i:
            delta = prices[j] - prices[i]
            if delta > max_profit:
                max_profit = delta
            j -= 1
            
    return max_profit



def buy_and_sell_stock(prices: List[int]) -> int:
    """
    Code includes a nested loop 
    Time complexity analysis:
        Single loop --> O(n)

    Space complexity analysis:
        We are only defining a handful of variables --> O(1)
    """
    min_buy = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_buy)
        min_buy = min(min_buy, prices[i])

    return max_profit