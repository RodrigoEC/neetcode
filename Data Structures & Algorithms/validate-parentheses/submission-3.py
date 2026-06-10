from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque([])


        chars = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for char in s:

            if char in chars.keys():
                print("hey")
                q.append(char)
            else:
                if len(q) == 0 or chars.get(q[-1]) != char:
                    return False
                
                q.pop()
        return len(q) == 0
