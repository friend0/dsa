class Parentheses:

    def __init__(self, s: str) -> None:
        self.s = s
        self.max_result = -1
        self.result = set()

    def remove_invalid(self):

        def dfs(s: str, i: int, result: str, balance: int):

            if i >= len(s):
                if balance == 0:
                    if len(result) > self.max_result:
                        self.result = set()
                        self.result.add(result)
                        self.max_result = len(result)
                    if len(result) == self.max_result:
                        self.result.add(result)
                return

            c = s[i]
            if c == "(":
                dfs(s, i + 1, result + c, balance + 1)
                dfs(s, i + 1, result, balance)
            elif c == ")":
                if balance > 0:
                    dfs(s, i + 1, result + c, balance - 1)
                dfs(s, i + 1, result, balance)
            else:
                result += c
                dfs(s, i + 1, result, balance)

        dfs(self.s, 0, "", 0)
        return list(self.result)


p = Parentheses(")(")
print(p.remove_invalid())
