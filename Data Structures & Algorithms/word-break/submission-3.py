class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # wordDict = ["apple","pen","ape"]
        #
        #               applepenapple
        #           
        #           penapple
        # x     apple
        #.    
        # 
        #
        #
        #
        #
        # 

        cache = {}

        def dfs(i, subword):

            if i == len(s):
                cache[i] = True
                return True
            elif i > len(s):
                cache[i] = False
                return False

            if i in cache:
                return cache[i]

            
            for word in wordDict:

                if word == subword[:len(word)]:
                    cache[i] = cache.get(i, False) or dfs(i + len(word), subword[len(word):])

            return cache[i] if cache.get(i) else False
        
        res = dfs(0, s)
        print(res)
        print(cache)
        return res






