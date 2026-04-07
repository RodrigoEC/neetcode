class Solution:
    def reverseBits(self, n: int) -> int:
        res = []
        print(n)
        str_int = f"{n:b}"
        str_int = "0" * (32 - len(str_int)) + str_int
        for i in range(len(str_int) - 1, -1, -1):
            res.append(str_int[i])


        max_power = len(str_int)
        print("".join(res), len(res))
        num = 0
        for i in range(len(res) -1, -1, -1):

            if res[i] == "1":
                print(2**(max_power - (i + 1)), i)
                num += 2**(max_power - (i + 1))

        return num