class Solution:
    def maximumSwap(self, number: int) -> int:
        """
        Мы должны один раз поменять местами числа в номере, чтобы он был
        максимальным
        :param number: number
        :return: max number
        """
        numbers_list = list(str(number))
        last = {int(d): i for i, d in enumerate(numbers_list)}
        for i, digit in enumerate(numbers_list):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    numbers_list[i], numbers_list[last[d]] = numbers_list[last[d]], numbers_list[i]
                    return int(''.join(numbers_list))
        return number

print(Solution().maximumSwap(2736))