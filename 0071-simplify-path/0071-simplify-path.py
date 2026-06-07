class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue
            elif stack and part == "..":
                stack.pop()
            elif not stack and part == "..":
                continue
            else:
                stack.append(part)

        return "/" + "/".join(stack)