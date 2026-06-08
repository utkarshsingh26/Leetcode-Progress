class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        parts = path.split("/")

        for part in parts:
            if part == "" or part == "." or (part == ".." and not stack):
                continue
            elif part == ".." and stack:
                stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)