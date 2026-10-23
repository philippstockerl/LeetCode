class Solution:
    def plusOne(
        self, 
        digits: list[int]
        ) -> list[int]:
        """
        Task    :   given a large integer represented as an integer array 'digits',
                    where each 'digits[i]' is the ith digit of the integer.
                    the digits are ordered from most significant to least significant
                    in left-to-right order.
                    the large integer does not contain any leading 0´s.
                    
                    increment the large integer by one and return the resulting array 
                    of digits.
                    
                    -   join() method takes all items in an iterable and joins them into
                        one string:
                        -------------------------
                        'string separator'.join()
                    
                    -   map() function executes a specified function for each item in an
                        iterable. the item is sent to the function as a parameter
                        ------------------
                        map(function, iterables)
        """
        
        number      = int("".join(map(str,digits)))
        return list(map(int, str(number + 1)))
        
        
    
    def main(self):
        digits  = [1,2,3]
        print(self.plusOne(digits))
        
        
        
        
if __name__ == "__main__":
    Solution().main()