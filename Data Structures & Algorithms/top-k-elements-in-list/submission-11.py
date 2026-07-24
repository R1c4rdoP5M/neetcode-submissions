from typing import List
from collections import Counter

class Solution:
    def getTop(self, counters: dict):
        max = 1
        
        for key, value in counters.items():
            if max < value:
                max = value
        for key, value in counters.items():
            if value == max:
                return key
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = {}
        for i in range(len(nums)):
            if nums[i] not in counters:
                counters[nums[i]] = 1
            else:
                counters[nums[i]] += 1

        tops = []
        for i in range(k):
            tops.append(self.getTop(counters))
            counters.pop(self.getTop(counters))
            
        return tops