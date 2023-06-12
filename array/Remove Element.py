class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ptr_num1 = 0
        ptr_num2 = len(nums) - 1

        while ptr_num2 > ptr_num1:
            if nums[ptr_num1] == val:
                while nums[ptr_num2] == val:
                    ptr_num2 -= 1
                nums[ptr_num1] , nums[ptr_num2] = nums[ptr_num2], nums[ptr_num1]
                ptr_num1 += 1
            else:
                ptr_num1 += 1 
        print(nums[:ptr_num2])
        return len(nums[:ptr_num2])      
        
if __name__ == "__main__":
    problem2 =  Solution()
    nums = [2] # Input array
    val = 3 # Value to remove
    k = problem2.removeElement(nums, val) # Calls your implementation

    print(k)
    print(nums)
    # nums = sorted(nums, 0, k); # Sort the first k elements of nums
    # for i in range(len(nums)):
        # print( nums[i] == expectedNums[i])


