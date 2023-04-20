class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        list1 = list(word1)
        list2 = list(word2)

        while list1 and list2:
            ans.append(list1.pop(0))
            ans.append(list2.pop(0))

        ans.extend(list1)
        ans.extend(list2)

        return "".join(ans)