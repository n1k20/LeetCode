class Solution:
    def addDigits(self, number: int) -> int:
        if number == 0: return 0
        elif number % 9 == 0: return 9
        else: return number % 9