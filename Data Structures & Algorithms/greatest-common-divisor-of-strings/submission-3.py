class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        

        # What we need to do?
        # We need to find the biggest substring that devides both
        # str1 and str2 n, m times
        #
        # e.g.: 
        # str1 = "ABAB" -> ABA
        # str2 = "AB" -> AB
        #  
        # answer = "AB"

        # How should we do it?
        # e.g. 1: 

        # str1 = "ABABAB"
        # str2 = "ABAB"
        # 
        #
        # 6 chars for str1
        # 4 chars for str2 <- going w/ this one
        #
        # 
        # is ABAB a good diviser for str1? (true?)
        #  -> is ABAB a good diviser for str2?
        # 
        # is ABA a good diviser for str1?
        # is AB a good diviser for str1? (yes)
        #  - is AB a good diviser for str2? (yes)
        #

        
        # What algorithm/structure am I using?
        # 
        #
        # 

        # What's the time and space complexity?
        # n = str1, m = str2
        # - time: O(m * n * m) -> O(max_len(m, n) * min_len(m,n)^2)
        # - 

        def is_divisor(sub_str, target):

            if len(sub_str) == len(target):
                return sub_str == target
            
            left, right = 0, len(sub_str)

            while right < len(target):
                print(left, right, sub_str, target[left: right])

                if sub_str == target[left: right]:
                    left = right
                    right += len(sub_str)
                else:
                    print(sub_str, False)
                    return False
            
            print(sub_str, right == len(target))
            return right == len(target) and sub_str == target[left: right]

        [divisor, target] = [str1, str2] if len(str1) < len(str2) else [str2, str1]


        for i in range(len(divisor), 0, -1):
            

            if is_divisor(divisor[:i], target):
                if is_divisor(divisor[:i], divisor):
                    return divisor[:i]
        
        return ""

        # str1 = NANANA
        # str2 = NANA

        
        # target = NANANA
        #
        # divisor = NANA
        #             |
        # 
        #










        