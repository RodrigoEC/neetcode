from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        # for each word we already have a lexicographical order,
        # so "hrn": h -> r -> n
        #           h -> r -> f
        #           e -> r
        #           e -> n
        #           r -> f -> n
        # 


        # We could create sort of a graph with dicts based on the 
        # first letters of the words

        # First step: Create a graph like dictonary representing the
        # order relationships between the chars.
        #
        #
        #
        # {"h": ["r"], "r": ["n", "f"], "e": ["r", "n"], "f": ["n"], "n": []}
        #
        # n -> f
        # h -> e
        # r -> n
        # e -> r
        #
        #
        #
        # Second step: We need to merge them by having a visited set of chars
        # and make sort of a 
        
        graph = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            fst_wrd = words[i]
            scd_wrd = words[i + 1]


            minLen = min(len(fst_wrd), len(scd_wrd))
            if len(fst_wrd) > len(scd_wrd) and fst_wrd[:minLen] == scd_wrd[:minLen]:
                return ""

            pointer = 0
            while pointer < len(fst_wrd) and pointer < len(scd_wrd) and fst_wrd[pointer] == scd_wrd[pointer]:

                pointer += 1
            
            if pointer == len(fst_wrd) or pointer == len(scd_wrd):
                continue

            graph[fst_wrd[pointer]].add(scd_wrd[pointer])
    
        print(graph)
        
        res = []
        
        visited = {}

        def dfs(char):

            if char in visited:
                return visited[char]

            
            visited[char] = True

            for neigh in graph[char]:
                if dfs(neigh):
                    return True
            
            visited[char] = False
            res.append(char)

        
        for char in graph:
            if dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)










