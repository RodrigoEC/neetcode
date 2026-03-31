class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # What we need to do? We need to run on the s2 string and check if
        # a substring of that string is a permutation of the s1 string. Something
        # to keep an eye on is thet fact that the string "abdc" is not a permutation
        # of the string "abc" even though it has the same chars

        # How should I do it? We need to iterate on the s2 string and while we're
        # iterating check if that subtring is a permutation of the s1 string. Here
        # everytime we get to a character that's on the s1 we should start a process
        # of checking if a subtring starting on that character is a permutation.
        # If we get to a point on process where we find a char that's not on s1, than
        # we need to discard this possible permutation

        # s1 = "abc", s2 = "lacabee"
        # pointer = 4
        # matches = 0

        # f1 = {a: 1, b: 1, c: 1}
        # window = {c: 1, a: 1, b: 1}


        # What structure/algorithm should I use? We can use a sliding window 
        # approach with a hashmap or hashset. I think I'm going to use a hashmap

        # What's the complexity?


        if len(s1) > len(s2): return False

        # s1 = abc

        # chars2 = [e, c, a, b]
        # s2 = lecabee
        #       L
        #          R

        chars1 = {}
        for char in s1:
            chars1[char] = chars1.get(char, 0) + 1

        chars2 = {}

        left = right = 0
        matches = 0
        while (right < len(s2)):
            
            if (right - left == len(s1)):
                if (s2[left] in chars1 and chars2[s2[left]] == chars1[s2[left]]):
                    matches -= 1

                chars2[s2[left]] -= 1
                left += 1
            

            chars2[s2[right]] = chars2.get(s2[right], 0) + 1
            if (s2[right] in chars1 and chars2[s2[right]] == chars1[s2[right]]):
                matches += 1

            right += 1

            if (matches == len(chars1.keys())):
                return True
            
        return False










