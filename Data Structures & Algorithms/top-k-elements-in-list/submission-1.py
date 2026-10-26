class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        # values_list = list(d.values())
        # values_list.sort()
        # l = values_list[-k:][::-1]
        sorted_keys = sorted(d, key=d.get)
        return sorted_keys[-k:]
        # for key,v in d.items():
        #     if v>=k:
        #         l.append(key)
        return l
        