class Solution:
    def isHappy(self, n: int) -> bool:
        

        seen = set()
        

        number = n
        while number not in seen:
            seen.add(number)
            new_num = 0
            str_num = str(number)

            for char in str_num:

                parsed_char = int(char)

                new_num += parsed_char * parsed_char
            
            if new_num == 1:
                return True
            
            number = new_num

        return False            