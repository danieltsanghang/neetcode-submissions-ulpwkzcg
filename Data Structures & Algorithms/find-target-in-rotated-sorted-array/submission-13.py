class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            c = (l+r) // 2
            print(nums[c])
            if nums[c] == target:
                print("found")
                return c
            else: 
                if nums[c] >= nums[l]: # left is sorted
                    if nums[l] <= target < nums[c]:
                        r = c - 1
                        print("in left inclusive start exclude end cause c != target")
                    else:
                        l = c + 1
                        print("not in left, discard left side")
                else: # right is sorted
                    if nums[c] < target <= nums[r]:
                        l = c + 1
                        print("in right inclusive end cause c != target")
                    else:
                        r = c - 1
                        print("not in right, discard right side")

        return l if nums[l] == target else -1