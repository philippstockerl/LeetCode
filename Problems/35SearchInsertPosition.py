class Solution:
    def searchInsert(
        self, 
        nums: list[int], 
        target: int
        ) -> int:
        
        """
        Task    :   given a sorted array of distinct integers and a target
                    value, return the index if the target is found.
                    if not, return the index where it would be if it were
                    inserted in order.
                    
                    algorithm must be written with O(log n) runtime complexity
                    
                    
        Approach:           
        """ 
        if target not in nums:
            nums.append(target)
            nums.sort()
            newIndex    = nums.index(target)
            nums.remove(target)
            return newIndex
                    
        else:
            return nums.index(target)

            
    def main(self):
        nums    = [1,3,5,6]
        target  = 7
        print(f"Output: {self.searchInsert(nums, target)}")
        
        
        
        
if __name__ == "__main__":
    Solution().main()