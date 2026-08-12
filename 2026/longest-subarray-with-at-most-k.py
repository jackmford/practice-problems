def longest_ones(nums, k):
    # while subarray contains > k zeroes, shrink window
    # if not, grow window
    left = 0
    zeroes = 0
    longest = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1

        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1

        longest = max(longest, right - left + 1)
    print(longest)
    return longest


nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
k = 2
print(longest_ones(nums, k))
