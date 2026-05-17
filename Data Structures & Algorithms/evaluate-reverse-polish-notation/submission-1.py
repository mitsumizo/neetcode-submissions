class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opt = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a / b),
        }

        target_list:list[int] = []

        for elm in tokens:
            if elm in opt:
                second = target_list.pop()
                first = target_list.pop()
                target_list.append(opt[elm](first, second))
            else:
                target_list.append(int(elm))

        return target_list.pop()