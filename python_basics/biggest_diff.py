# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 

# biggest_diff([10, 3, 5, 6]) → 7
# biggest_diff([7, 2, 10, 9]) → 8
# biggest_diff([2, 10, 7, 2]) → 8

def biggest_diff(nums):
    largest,smallest = nums[0],nums[0]
    for x in range(0,len(nums)):
        if ( nums[x] > largest ):
            largest = nums[x]
        if ( nums[x] < smallest ):
            smallest = nums[x]           
    return largest - smallest
