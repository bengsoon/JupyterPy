# JupyterPy Documentation and Example

## Description
Automation API to convert Jupyter Notebook (.ipynb) JSON format into Python file (.py), with the capabilities to add magic functions to determine which cells to be exported.

## Installation

```
pip install JupyterPy
```

## How To Use It?
1. Develop the code in Jupyter Notebook / Lab just like how you'd normally do.

2. Make sure to separately import JupyterPy package.

``` Python
from JupyterPy.core import j2p
```

3. Tag the default magic function (`#@EXPORT`) at the top of each code cell that you'd want to export.

``` Python
#@EXPORT
import regex as re

# Define a class to check a Palindrome number
class Check :

    # Constructor
    def __init__(self,number) :
        self.num = number
```

4. Once you are ready to export your code, press `Ctrl+S` or `Cmd+S` to save your notebook.

5. Export your `.ipynb` notebook to `.py` file:

``` Python
# enter the filename of this jupyter notebook (don't forget the ".ipynb" extension!)
jupyter_file = r"./Example.ipynb"
target_py_file = "./JupyterPytest.py"

# export the notebook to .py 
j2p(jupyter_file=jupyter_file, output_file=target_py_file)
```

## See It In Action


```python
from JupyterPy.core import JupyterPy as j2p
```

This is where we can develop and test our codes in our Notebook just like how we'd normally do, except that we will tag only the cells that we'd want to export into the `.py` file with the default magic function (`#@EXPORT`)

For `j2p` to know which cell to export, the `#@EXPORT` magic function has to be tagged at the top of the code cells that we'd want to export.

### Start of our code development


```python
#@EXPORT
## This will be the first line comment
import regex as re

## Insert a space under each cell for code readability

```


```python
print("This line of code will not show up in our JupyterPytest.py file")
```

    This line of code will not show up in our JupyterPytest.py file



```python
#@EXPORT
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
            
```


```python
#@EXPORT
def check_this_palindrome(number):
    return Check(number).isPalindrome()

```

Let's test our class on this notebook, but _these cells will not be exported_ as we are not tagging them with our magic function (we would not want our tests to be in our `.py` file)


```python
# input a palindrome example
num_palindrome = 185581
```


```python
check_this_palindrome(num_palindrome)
```

    185581 is Palindrome



```python
# input a non-palindrome example
num_notpalindrome = 188581
```


```python
check_this_palindrome(
    num_notpalindrome)
```

    188581 is not Palindrome


### Export to `JupyterPytest.py`

Now that we're done with our code, let's finally export it! 

But before we do so, we have to make sure to **SAVE OUR NOTEBOOK** (press `Ctrl+S`), otherwise we won't get the latest update from our code!

Once we have saved the notebook, we then need to specify the filename of this Jupyter Notebook (don't forget the `.ipynb` extension!)


```python
# enter the filename of this jupyter notebook (don't forget the ".ipynb" extension!)
jupyter_file = r"./Example_single_file.ipynb"
target_py_file = "./JupyterPytest.py"
```

We will now export the Notebook to `.py` file


```python
# export the notebook to .py
j2p(jupyter_file=jupyter_file, output_file=target_py_file)
```




    Extracted '#@EXPORT' codes from Example_single_file.ipynb into JupyterPytest.py



### Check our output `JupyterPytest.py`


```python
!cat JupyterPytest.py
```

    
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


## Custom Magic Functions and Multiple `.py` targets

`j2p` can also be used with multiple custom magic functions and `.py` functions. For more information, please check out the `Example_multiple.ipynb`
