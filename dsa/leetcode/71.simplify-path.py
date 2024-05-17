#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:

    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for elem in path:
            if stack and elem == "..":
                stack.pop()
            elif elem not in ["", ".", ".."]:
                stack.append(elem)
        return "/" + "/".join(stack)


# @lc code=end
