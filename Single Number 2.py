from typing import List
class Solution:
    def singleNumber(self, numbers: List[int]) -> List[int]:
        if len(numbers) == 2:
            return numbers
        ones, twos = set(), set()
        for number in numbers:
            if number not in ones: ones.add(number)
            else: twos.add(number)
        return list(ones - twos)