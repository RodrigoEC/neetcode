class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # What we need to do?

        # We're given a string that represents a path for
        # a directory. We need to simplify this path as much
        # as possible
        #
        # e.g.:
        # input -> "/neetcode/practice//...///../courses"
        # output -> "/neetcode/practice/courses"
        #
        # input -> neetcode
        # 



        # How should we do it?
        # 
        #

        # What's the time and space complexity:
        # - Time: O(n)
        # - space: O(n)
        # 


        stack = []

        pointer = 0
        while pointer < len(path):

            if path[pointer] == "/":
                pointer += 1
                continue
            
            directory = ""
            while pointer < len(path) and path[pointer] != "/":
                directory += path[pointer]
                pointer += 1
            
            if directory == "." or directory == "":
                continue
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
            

        return f"/{"/".join(stack)}"








