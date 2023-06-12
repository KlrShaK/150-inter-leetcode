
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_num1 = m - 1
        ptr_num2 = n - 1
        ptr_itr = m + n - 1   
        
        if ptr_num1 < 0:
            nums1[ptr_itr] = nums2[ptr_num2]

        while ptr_itr >= 0 : # and ptr_num1 <= ptr_itr
            if nums1[ptr_num1] >= nums2[ptr_num2] and ptr_num1 >= 0:
                nums1[ptr_itr] = nums1[ptr_num1]
                ptr_num1 -= 1 
                ptr_itr -= 1

            elif nums1[ptr_num1] <  nums2[ptr_num2] and ptr_num2 >= 0:
                print(ptr_num2, ptr_itr)
                nums1[ptr_itr] = nums2[ptr_num2]
                ptr_num2 -= 1 
                ptr_itr -= 1
            
            if ptr_num2 >= 0 and ptr_num1 <= -1:
                nums1[ptr_itr] = nums2[ptr_num2]
                ptr_num2 -= 1 
                ptr_itr -= 1
            if ptr_num1 >= 0 and ptr_num2 <= -1:
                nums1[ptr_itr] = nums1[ptr_num1]
                ptr_num1 -= 1 
                ptr_itr -= 1
        
if __name__ == "__main__":
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3

    problem1 =  Solution()
    problem1.merge(nums1, m, nums2, n)
    print(nums1)

