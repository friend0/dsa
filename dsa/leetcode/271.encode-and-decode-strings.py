#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start
from unicodedata import digit


class Codec:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = []
        for s in strs:
            res.append(str(len(s)) + "\r" + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        results = []
        i = 0
        # print(s)
        while i < len(s):
            digit_end = i
            while s[digit_end] != '\r':
                digit_end += 1
            digit_end += 1
            read_bytes = int(s[i:digit_end])
            results.append(s[digit_end:digit_end + read_bytes])
            i = digit_end + read_bytes

        return results


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end
