class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        init, end = 0, len(s) - 1
        while init < end:
            s[end], s[init] = s[init], s[end]
            init += 1
            end -= 1
        
