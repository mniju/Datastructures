## Single Element in a sorted Array

Leet Code challenge 540

Difficulty: Medium

*Problem:* You are given a sorted array consisting of only integers where 
every element appears exactly twice, except for one element which appears exactly once. 
Find this single element that appears only once.

The solution should run in O(logn) and O(1) space.

    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2

    Input: nums = [3,3,7,7,10,11,11]
    Output: 10

*Thought Process*
  1. We can traverse through the list  and find if the next elemnt is the same for alternate indices. This would mean , runtime of O(n)
  2. We can have Hastables for all the elemnts in the array and then find the element that repeats once. This takes the O(n) space.
  3. Since we are asked with runtime of O(logn) we need to use something like binary tree.

* The observation is that the pair elements will occur in this fashion(evenindex, oddindex).
* We will find a middle point in the list . 
* If the middle point is even , then the element in next index should match or if the midpoint is Odd, the element in previous index should match with the middle element.
  * if it matches , then there is no unique element until this index.So start the search in the right half of the list.
  * if its doesnt match , start the search in the left half of the Midpoint.

My Solution for this is 

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while (l<r):
            mid = l+(r-l)//2
            if mid%2 ==0 :
                # If even , it should match with next digit
                if nums[mid]==nums[mid+1]:
                    l= mid+2
                else:
                    r=mid-1
            else:
                # If odd , it should match with prev digit
                if nums[mid]==nums[mid-1]:
                    l = mid+1
                else:
                    r= mid-1
        return nums[l]

```
 found a clever solution in leet code siscussion forum that uses XOR function to compare the the element corresponding to the odd even midpoint rather than explicitly checking if the midpoint is odd/even

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) //2
            if nums[m] == nums[m^1]:
                l = m + 1
            else:
                r = m
        return nums[l]
```


## Remove K Digits

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        digits_to_remove = k
        stack =[]
        #print(num)
        #if len(num)==k : return "0" # Handled in the last length case
        for digit in num:
            while digits_to_remove>0 and stack and digit < stack[-1]: 
                '''
                If we are not yet done with removing teh digits  and 
                stack is not empty (it will be empty in iter 0)
                and the current number is  less than the top number in stack
                '''
                stack.pop()
                digits_to_remove-=1
            stack.append(digit)
            
        '''
        (1)if the numbers are in ascending order - 12345678
        then the current number will always be greater than the 
        previous digit . And our above algorithm doesnt handle that .
        So in the end remove the remainig 'k' elemnts from teh string.
        (2)Remove trailing zeros
        
        '''

        result = "".join(stack[0:len(num)-k]).lstrip("0")    
        
        '''
        If there is no element after the removal of the zeros, #then returen "0"
        '''

        if len(result):
            return result
        else:
            return "0"
        return result
```

Another Sleek soln from leet code forum:

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        return ''.join(stack[:-k or None]).lstrip('0') or '0'
```