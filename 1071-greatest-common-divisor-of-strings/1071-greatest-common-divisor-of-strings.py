class Solution:
    def getSharedPrefix(self, str1, str2):
        i = 0
        while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
            i += 1
        return str1[:i]
    
    def cleanlyDivides(self, prefix, string):
        if len(string) % len(prefix) != 0:
            return False
        return prefix * (int(len(string) / len(prefix))) == string
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prefix = self.getSharedPrefix(str1, str2)
        while prefix:
            if self.cleanlyDivides(prefix, str1) and self.cleanlyDivides(prefix, str2):
                break
            else:
                prefix = prefix[:-1]
        return prefix
            