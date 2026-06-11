class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=""
        for char , char2 in zip(word1,word2):
            result+=(char+char2)

        if len(word1)>len(word2):
            result+=word1[len(word2):]
        if len(word1)<len(word2): 
            result+=word2[len(word1):]

        return result