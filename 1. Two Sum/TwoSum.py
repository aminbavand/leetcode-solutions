class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {}
        for num in nums:
            diffDict.update({num:target-num})
        for num in diffDict:
            if diffDict.get(diffDict.get(num)) is not None:
                first_ind = list(diffDict.keys()).index(num)
                second_ind = list(diffDict.keys()).index(target-num)
                if first_ind!=second_ind:
                    return [first_ind,second_ind]
        new_list = [i for i in range(len(nums)) if nums[i] == target/2] 
        return new_list