class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for val in strs:
            mp = [0]*26
            for i in val:
                mp[ord(i) - ord('a')] += 1
            hm[tuple(mp)].append(val)
        return list(hm.values())