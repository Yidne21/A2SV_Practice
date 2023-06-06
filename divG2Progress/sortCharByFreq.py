class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        sortedmap = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        ans = []
        for i in sortedmap.keys():
            freq = hashmap[i]
            for j in range(freq):
                ans.append(i)
        return ''.join(ans)
