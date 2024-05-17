from typing import List


class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i, char in enumerate(order):
            order_dict[char] = i

        for w1, w2 in zip(words, words[1:]):
            for i in range(min(len(w1), len(w2))):
                c1, c2 = w1[i], w2[i]
                if order_dict[c1] < order_dict[c2]:
                    break
                elif order_dict[c1] > order_dict[c2]:
                    return False
                elif i == min(len(w1), len(w2)) - 1:
                    if len(w1) > len(w2):
                        return False
        return True
