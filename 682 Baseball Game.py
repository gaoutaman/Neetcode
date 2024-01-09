# My first try
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        sum = 0
        scores = []
        for operation in operations:
            if operation == "+":
                scores.append(scores[-1] + scores[-2])
                sum += scores[-1]
            elif operation == "C":
                re = scores.pop()
                sum -= re
            elif operation == "D":
                scores.append(2 * scores[-1])
                sum += scores[-1]
            else:
                scores.append(int(operation))
                sum += scores[-1]
        return sum


## Don't need to keep track of sum as you can just sum(scores)
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []
        for operation in operations:
            if operation == "+":
                scores.append(scores[-1] + scores[-2])
            elif operation == "C":
                scores.pop()
            elif operation == "D":
                scores.append(2 * scores[-1])
            else:
                scores.append(int(operation))
        return sum(scores)
