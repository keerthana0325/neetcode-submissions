class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_list = list(magazine)
        flag = True
        for i in range(len(ransomNote)):
            if ransomNote[i] not in char_list:
                flag = False
                break
            if ransomNote[i] in char_list:
                char_list.remove(ransomNote[i])
        return flag

        