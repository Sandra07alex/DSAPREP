# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# Time: O(log x)
# Space: O(1)
# 2^31-1 is the max value of integer
#  
x = int(input("Enter a non-negative integer: "))

if x < 2:
    print(x)
else:
    left = 1
    right = x // 2
    answer = 0

    while left <= right:

        mid = left + (right - left) // 2
        sqr = mid * mid

        if sqr == x:
            answer = mid
            break

        elif sqr <= x:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1

    print("Integer square root:", answer)

        