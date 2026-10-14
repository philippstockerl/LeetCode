class Solution:
    def isPalindrome(
            self, 
            x: int
            ) -> bool:

        """
        Task        :   Define a function that checks if a number is a palindrome number.
        Approach    :   Split number into its digits and insert into list to then check if the
                        reversed list equals input
        """
        digitList           = [int(d) for d in str(x)]
        reversedDigitList   = digitList[::-1]

        for index,value in enumerate(digitList):
            if value != reversedDigitList[index]:
                return False

        return True

    
    def main(self):
        numberToCheck = 98
        print(self.isPalindrome(numberToCheck))


if __name__ == "__main__":
    Solution().main()