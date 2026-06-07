class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        parts = path.split("/")

        for part in parts:
            if (part == "") or (part == ".") or (not stack and part == ".."):
                continue
            elif stack and part == "..":
                stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)