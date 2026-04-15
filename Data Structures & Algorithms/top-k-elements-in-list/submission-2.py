class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_freq = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        for num, freq in num_freq.items():
            buckets[freq].append(num)

        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result