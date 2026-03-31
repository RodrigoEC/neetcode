class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        

        # What we need to do?
        #
        # We're given two string numbers and we need to multiply them
        # without using any built-in library for converting types.
        #
        # e.g.: 
        # num1 = "3" num2 = "4"
        # output = "12"

        # How should we do it?
        #
        # result = []
        #
        # num1 = "111", num2 = "222"
        #
        #       222
        #   | x111
        #      ----
        #       222 
        #      222
        #.    222
        #.   [24642]

        # num1 = "191", num2 = "222"
        # 
        #       222
        #   | x191
        #      ----
        #       222 
        #.    1998
        #.    222 
        #.   [42402]

        #.        p
        #   [2,10,13,11,3]
    #.               M
        #   [2,0,4,2,4]      
        #
        # What structure/algorithm can we use?
        #
        #


        # What's the time and space complexity of this approach?
        # - Time: O(m * n), where m = len(num1), n = len(num2)
        # - Space: O()
        if num1 == "0" or num2 == "0": return '0'

        result = []
        start = 0

        for i1 in range(len(num1) -1, -1, -1):
            pointer = start
            for i2 in range(len(num2) -1, -1, -1):
                
                local_prod = int(num1[i1]) * int(num2[i2])
                print(local_prod)

                query = 0
                if local_prod >= 10:
                    query = local_prod // 10
                    local_prod = local_prod % 10

                if pointer == len(result):
                    result.append(local_prod)
                else:
                    result[pointer] += local_prod

                if query:
                    if pointer + 1 >= len(result):
                        result.append(query)
                    else:
                        result[pointer + 1] += query

                
                pointer += 1
            
            start += 1
        

        for i, num in enumerate(result):
            if num >= 10:
                query = result[i] // 10
                result[i] = result[i] % 10

                if i == len(result) - 1:
                    result.append(query)
                else:
                    result[i + 1] += query
            



        print(result)


        result.reverse()
        return "".join([f"{num}" for num in result])
                    
















