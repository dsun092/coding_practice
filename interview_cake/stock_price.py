
def max_profit(arr):
    #Input: Array of unsorted integers
    #Output: Max difference within the array.
    if len(arr) < 2:
        return None
    cur_min = arr[0]
    max_profit = arr[1] - arr[0]

    for i in xrange(1, len(arr)):
        cur_profit = arr[i] - cur_min
        max_profit = max(max_profit, cur_profit)
        cur_min = min(cur_min, arr[i])

    return max_profit


def product_of_all(arr):
    output_arr = [1] * len(arr)
    cur_product = 1
    for i in xrange(1, len(arr)):
        cur_product *= arr[i-1]
        output_arr[i] = cur_product

    cur_product = 1
    for i in xrange(len(arr)-2, -1, -1):
        cur_product *= arr[i+1]
        output_arr[i] *= cur_product
    return output_arr


def highest_product_of_3(arr):
    if len(arr) < 3:
        return -1
    max_three = 0
    max_two = arr[0] * arr[1]
    max_one = max(arr[0], arr[1])
    min_two = arr[0]*arr[1]
    min_one = min(arr[0], arr[1])

    for i in xrange(2, len(arr)):
        max_three = max([max_three, max_two*arr[i], min_two*arr[i]])
        max_two = max(max_two, max_one * arr[i], min_one*arr[i])
        min_two = min(min_two, max_one * arr[i], min_one*arr[i])
        min_one = min(min_one, arr[i])
        max_one = max(max_one, arr[i])
    return max_three

