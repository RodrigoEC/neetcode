class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        # What we need to do? We to find and add all possible combinations
        # for these digits. There's not much to it

        # How should we do it? We could use a DFS/BFS to store these numbers and
        # make all the possible combinations

        # What structure/algorithm should we use? We're going to use BFS on this
        # just to train

        # What's the time complexity of this approach? O(number of digits * median number
        # of characters mapped for each digit)

        mapDigits = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if not len(digits): return []

        q = deque(digit for digit in mapDigits[digits[0]])

        for i in range(1, len(digits)):

            for _ in range(len(q)):
                
                combination = q.popleft()

                for char in mapDigits[digits[i]]:
                    q.append(f'{combination}{char}')

        

        return list(q)



