class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        int_array_set = set()
        
        for num in nums:
            if num in int_array_set:
                return True
            else:
                    int_array_set.add(num)
                    # value = False
        return False