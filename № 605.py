from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], number: int) -> bool:
        if number == 0: return True
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and
                    (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1
                number -= 1
                if number == 0:
                    return True
        return False


