from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        set_arr = set(nums)
        new_count = 1
        if nums == []:
            return 0
        for i in nums:
            hash_map[i] = i
        for i in set_arr:
            count = 1
            next_val = i + 1
            while hash_map.get(next_val, None) != None:
                next_val += 1
                count += 1
            if count > new_count:
                new_count = count

        return new_count 


    
sol  = Solution()
print(sol.longestConsecutive([2,20,4,10,3,4,5]))