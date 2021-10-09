import re
def tgen(text):
    return re.sub("[^A-Za-z0-9]+", "", text).lower()
class Solution:
    def isPalindrome(self, s: str) -> bool:
         return tgen(s) == tgen(s)[::-1]