class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtered_s = "".join(char for char in s if char.isalnum()).lower()
        print(filtered_s)
        init, end = 0, len(filtered_s) - 1
        
        while init < end:
            if filtered_s[init] != filtered_s[end]:
                return False

            init += 1
            end -= 1
        
        return True