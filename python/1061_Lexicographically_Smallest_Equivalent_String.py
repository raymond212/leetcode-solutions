class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        groups = [] # each group contains equivalent characters
        belong = {x: -1 for x in ascii_lowercase} # mapping from character to group index
        for i in range(len(s1)):
            a = s1[i]
            b = s2[i]
            first_match = -1 # index of first group that contains a or b
            for j, group in enumerate(groups):
                if a not in group and b not in group:
                    continue 
                elif a in group:
                    group.add(b)
                    belong[b] = j
                elif b in group:
                    group.add(a)
                    belong[a] = j
                else:
                    first_match = -2 # previously processed case
                    break
                first_match = j
                break
            if first_match == -2:
                continue
            elif first_match == -1:
                new_group = {a, b}
                belong[a] = len(groups)
                belong[b] = len(groups)
                groups.append(new_group)
            else:
                for j in range(first_match + 1, len(groups)): # merge all other groups that contain a or b into the first match
                    group = groups[j]
                    if a not in group and b not in group:
                        continue 
                    for c in group:
                        belong[c] = first_match 
                        groups[first_match].add(c)
        ans = []
        for c in baseStr:
            if belong[c] == -1: # no alternative
                ans.append(c)
                continue 
            min_char = c 
            for d in groups[belong[c]]:
                if d < min_char:
                    min_char = d 
            ans.append(min_char)
        return "".join(ans)