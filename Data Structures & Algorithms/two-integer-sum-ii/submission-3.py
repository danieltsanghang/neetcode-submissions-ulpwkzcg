class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pos = 0
        right_pos = len(numbers) - 1
        
        while left_pos < right_pos:
            sum_ = numbers[left_pos] + numbers[right_pos]
            if sum_ == target:
                return [left_pos+1, right_pos+1]
            elif sum_ < target:
                left_pos += 1
            elif sum_ > target:
                right_pos -= 1