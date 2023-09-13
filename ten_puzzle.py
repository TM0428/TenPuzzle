import itertools
from typing import List, Any, Callable

class TenPuzzle:
    n: int
    m: float
    a: List[float]
    calc: List[Callable[[float, float], float]] = [lambda a, b:a + b, lambda a, b:a - b, lambda a, b:a * b, lambda a, b:a / b]
    sign = ["+", "-", "x", "/"]

    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a

    def solver(self, arr) -> List[Any]:
        if len(arr) == 2:
            ans: List[Any] = []
            for i in range(len(self.calc)):
                try:
                    if self.calc[i](arr[0], arr[1]) == self.m:
                        ans.extend(["(", str(arr[0]), self.sign[i], str(arr[1]), ")"])
                        return ans
                except ZeroDivisionError:
                    return []
            return ans

        for i in range(len(arr) - 1):
            for j in range(len(self.calc)):
                try:
                    next: List[float] = arr[:i] + [self.calc[j](arr[i], arr[i + 1])] + arr[i + 2:]
                except ZeroDivisionError:
                    return []
                ans = self.solver(next)
                if len(ans) != 0:
                    try:
                        calc_result = self.calc[j](arr[i], arr[i + 1])
                    except ZeroDivisionError:
                        return []
                    k = ans.index(str(calc_result))
                    ans[k:k + 1] = ["(", str(arr[i]), self.sign[j], str(arr[i + 1]), ")"]
                    return ans
        return []

    def print(self, a: List[Any]):
        # 最外の括弧を外す
        del a[0]
        del a[len(a) - 1]
        for i in range(len(a) - 1, 1, -1):
            if a[i] == "+" or a[i] == "-":
                if (a[i - 1] == ")"):
                    # この括弧はいらない
                    del a[i - 1]
                    imos = 0
                    for j in range(i - 2, -1, -1):
                        if a[j] == ")":
                            imos += 1
                        if a[j] == "(":
                            if imos == 0:
                                del a[j]
                                break
                            else:
                                imos -= 1


        print(''.join(a))
        return ''.join(a)


    def solve(self):
        perm = list(itertools.permutations(self.a))
        for x in perm:
            x = list(x)
            ans = self.solver(x)
            if len(ans) != 0:
                self.print(ans)
                return
        return 0


if __name__ == "__main__":
    puzzle = TenPuzzle(6, 13, [1, 2, 3, 3, 3, 9])
    puzzle.solve()
