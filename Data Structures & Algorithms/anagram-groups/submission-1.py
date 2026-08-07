class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        mp={}
        for i in range(len(s)):
            key="".join(sorted(s[i]))
            if not key in mp:
                mp[key]=[]
            mp[key].append(s[i])
        return list(mp.values())