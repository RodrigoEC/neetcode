class Solution:
    def climbStairs(self, n: int) -> int:
        

        # What we need to do?
        # n = 3
        # 1 + 1 + 1
        # 1 + 2
        # 2 + 1
        # 
        #
        # 
        #       |-
        #     |-
        #   |-
        # |-
        #


        res = [0] * (n + 2)
        res[n] = 1
        n -= 1

        while n >= 0:
            print(res, n)
            res[n] += res[n + 1] + res[n + 2]
            n -= 1
        

        return res[0]



        


