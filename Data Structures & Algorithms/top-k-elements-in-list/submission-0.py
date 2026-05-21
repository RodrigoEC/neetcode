from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freqs = defaultdict(int)

        max_freq = 0
        for num in nums:
            freqs[num] += 1

            max_freq = max(freqs[num], max_freq)
        
        res = []
        while len(res) < k:
            for element, freq in freqs.items():

                if freq == max_freq:
                    res.append(element)
                    
            max_freq -= 1

        return res
        

        