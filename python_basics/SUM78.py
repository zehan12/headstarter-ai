# Write a function to return the sum of the numbers in the given array 'nums', except ignore sections of numbers starting with a 7 and extending to the next 8 (every 7 will be followed by at least one 8). 
# Return 0 for no numbers.

# sum78([1, 2, 2]) → 5
# sum78([1, 2, 2, 7, 99, 99, 8]) → 5
# sum78([1, 1, 7, 8, 2]) → 4

def sum78(nums):
    total_sum = 0
    is_btw = False
    
    for num in nums:
        if num == 7:
            is_btw = True
        elif num == 8 and is_btw:
            is_btw = False
        elif not is_btw:
            total_sum += num
    
    return total_sum
