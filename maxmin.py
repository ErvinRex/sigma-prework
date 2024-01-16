test_arr = [100, -100]

# initialise function


def min_max(arr):
    # initialise the minimum and maximum value
    min_val = arr[0]
    max_val = arr[0]
    # for loop through the array for each number to be compared
    for num in arr:
        # if number is larger than the first in the array
        if num > max_val:
            # make the new number the max value and continue
            max_val = num
        # if number is smaller than the first in the array
        if num < min_val:
            # make the new number the min value and continue
            min_val = num
        # print the minimum and maximum value as an array
    print([min_val, max_val])


min_max(test_arr)
