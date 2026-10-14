class Solution:
    def twoSum(
        self, 
        nums: list[int], 
        target: int
        ) -> list[int]:

        """
        Task        :   Return the indices of the two integers in the list that add up to target value.

        Assumption  :   There is exactly one solution.

        Solution    :   Iterate over all possible number combinations using the list indices.
                        First loop for base number
                        Second loop for following numbers
                        If first loop number + second loop number = target, return indices as list
        
        """
        

        # Each for loop is O(n), so O(n^2)
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

            

    



    def main(self):
        nums    = [2,7,11,15]
        target  = 9
        print(self.twoSum(nums, target))

if __name__ == "__main__":
    Solution().main()