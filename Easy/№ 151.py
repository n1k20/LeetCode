class Solution:
    def reverseWords(self, words: str) -> str:
        """
        :type words: List[str]
        :param words: набор слов в виде строки
        :return: перевернутый список
        """
        return ' '.join((words.split()[::-1]))


