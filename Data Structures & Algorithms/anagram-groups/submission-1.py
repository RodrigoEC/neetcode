from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        # act -> [1, 0, 1, 0,0,0,0,0 [...], 0, 0,0,0,0]

        words = [word.lower() for word in strs]

        print(words)
        anagrams = defaultdict(list)
        for word in strs:
            alphaList = [0] * 27

            for char in word:
                pos = ord(char) - ord("a") + 1
                alphaList[pos] += 1
            
            key = ""
            for i, num in enumerate(alphaList):
                if not num:
                    continue 

                char = chr(96 + i)
                key += f"{char}{num}"

            anagrams[key].append(word)
        
        print(anagrams.values())
        return list(anagrams.values())





