
## This will be the first line comment
import regex as re

## Insert a space under each cell for code readability

# Define a class to check a Palindrome number
## Reference: https://www.includehelp.com/python/program-to-check-palindrome-number-using-object-oriented-approach.aspx
class Check :

    # Constructor
    def __init__(self,number) :
        self.num = number
        
    # define a method for checking number is Palindrome or not 
    def isPalindrome(self) :

        # copy num attribute to the temp local variable
        temp = self.num

        # initialise local variable result to zero
        result = 0

        # run the loop untill temp is not equal to zero
        while(temp != 0) :
            
            rem = temp % 10

            result =  result * 10 + rem

            # integer division
            temp //= 10

        # check result equal to the num attribute or not
        if self.num == result :
            print(self.num,"is Palindrome")
        else :
            print(self.num,"is not Palindrome")
            
def check_this_palindrome(number):
    return Check(number).isPalindrome()
