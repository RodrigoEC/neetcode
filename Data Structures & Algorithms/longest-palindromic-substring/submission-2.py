class Solution:
    def longestPalindrome(self, s: str) -> str:
        


        # [a] -> [a,a,a]
        # [] -> [a,a]


        # s = ababd
        #          
        # 
        def find_biggest_pal(start, end):
            
            biggest_pal = ""
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    if start != end:
                        
                        biggest_pal = s[start] + biggest_pal

                    biggest_pal += s[end]

                else:
                    return biggest_pal
                
                start -= 1
                end += 1

            return biggest_pal





        biggest_pal = ""
        for i, char in enumerate(s):

            pal = find_biggest_pal(i, i)
            pal_2 = find_biggest_pal(i, i + 1)
            
            if len(pal) > len(biggest_pal):
                biggest_pal = pal

            if len(pal_2) > len(biggest_pal):
                biggest_pal = pal_2
        

        return biggest_pal
