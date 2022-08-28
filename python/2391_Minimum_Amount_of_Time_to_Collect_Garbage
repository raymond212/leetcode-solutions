class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        rightG = 0
        rightP = 0
        rightM = 0
        totalG = 0
        totalP = 0
        totalM = 0
        for i in range(len(garbage)):
            s = garbage[i]
            glassCount = s.count("G")
            paperCount = s.count("P")
            metalCount = s.count("M")
            totalG += glassCount
            totalP += paperCount
            totalM += metalCount
            if glassCount > 0:
                rightG = i
            if paperCount > 0:
                rightP = i
            if metalCount > 0:
                rightM = i
        prefixSums = [0] * len(garbage)
        for i in range(len(travel)):
            prefixSums[i + 1] = prefixSums[i] + travel[i]
        res = totalG + totalP + totalM + prefixSums[rightG] + prefixSums[rightP] + prefixSums[rightM]
        return res
        
        