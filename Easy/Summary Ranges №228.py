from typing import List
class Solution:
    def summaryRanges(self, numbers: List[int]) -> List[str]:
        result = []
        for number in numbers:
            if result and result[-1][1] == number - 1: result[-1][1] = number
            else: result.append([number, number])
        return [f"{x}->{y}" if x != y else f"{x}" for x, y in result]