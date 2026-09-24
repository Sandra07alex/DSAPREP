# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# The key idea is: each comparison removes half of the search space.
# ⏱️ Time: O(log n)
# 💾 Space: O(1)
# Best case is O(1), when the target is found at the middle in the first comparison. Worst case is O(log n), because the search space is divided by half at every step.



nums = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("Target found at index:", mid)
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

else:
    print("Target not found")