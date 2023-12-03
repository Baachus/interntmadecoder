"""
Solving Leet Code problems
"""

from numpy import true_divide


def leet_code_27():
    """
    https://leetcode.com/problems/remove-element/
    """
    removal_list = [2, 8, 6, 3, 3, 5, 3, 2]
    target = 2

    def remove_element(list_to_remove, target):
        """
        Module to remove target from list
        """
        while target in list_to_remove:
            list_to_remove.remove(target)

    remove_element(removal_list, target)
    print(f'Remove element in list result: {removal_list}')

def leet_code_two_sum():
    """
    https://leetcode.com/problems/two-sum/
    """
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], start=i+1):
                if num1 + num2 == target:
                    return [i, j]

    list_to_search = [2,7,11,15]
    target = 26
    found_two = two_sum(list_to_search, target)
    print(f'Found two sum result: {found_two}')

def leet_code_palindrome_number():
    """
    https://leetcode.com/problems/palindrome-number/
    """
    def is_palindrome(number):
        """
        :type number: int
        :rtype: bool
        """
        reverse_number = str(number)[::-1]
        return str(number)==reverse_number

    number_to_test = 121
    print(f'The number {number_to_test} is a palindrome: {is_palindrome(number_to_test)}')

def leet_code_roman_to_integer():
    """
    https://leetcode.com/problems/roman-to-integer/
    """
    def roman_to_int(s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        value = 0
        i = 0
        while i < len(s):
            # Check if this is a subtractive combination
            if i + 1 < len(s) and s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                value -= symbols[s[i]]
                value += symbols[s[i+1]]
                i += 2
            # Else it's a normal Roman numeral
            else:
                value += symbols[s[i]]
                i += 1
        return value

    number = 'MCMXCIV'
    print(f'The roman number {number} is {roman_to_int(number)}')

def leet_code_remove_duplicates_from_array():
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    """
    def remove_duplicates(nums):
        """
        assumptions that array is sorted
        :type nums: List[int]
        :rtype: int
        """
        x = 1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[x] = nums[i+1]
                x+=1
        return x

    array = [0,0,1,1,1,2,2,3,3,4]
    print(f'The removal of duplicates results in {remove_duplicates(array)}')

def leet_code_3_sum():
    """
    https://leetcode.com/problems/3sum/
    """
    def three_sum(nums):
        """
        Returns triplets that are 3 distinct numbers and value of three added together = 0
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid, right = left+1, len(nums) - 1
            while mid < right:
                s = nums[left] + nums[mid] + nums[right]
                if s < 0:
                    mid +=1 
                elif s > 0:
                    right -= 1
                else:
                    triplets.append((nums[left], nums[mid], nums[right]))
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return triplets

    nums = [-1,0,1,2,-1,-4]
    print(f'The triplets are {three_sum(nums)}')

# leet_code_27()
# leet_code_two_sum()
# leet_code_palindrome_number()
# leet_code_roman_to_integer()
# leet_code_remove_duplicates_from_array()
leet_code_3_sum()
