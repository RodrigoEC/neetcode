class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        freq = {}

        for num in nums:
            if freq.get(num, False): return True


            freq[num] = True
        
        return False