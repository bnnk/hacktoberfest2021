class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return self.altin(word1,word2)
    def altin(self, text1, text2):
        textqr = ""
        using_len = min(len(text1),len(text2))
        for i in range(using_len):
            textqr += text1[i]
            textqr += text2[i]
        max_len = max(len(text1),len(text2))
        if(max_len == len(text1)):
            textqr += text1[i+1:]
        elif(max_len == len(text2)):
            textqr += text2[i+1:]
        return textqr

mergeAlt = Solution().mergeAlternately