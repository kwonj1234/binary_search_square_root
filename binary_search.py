#Find the square root of a number using binary search to within 3 decimal places
def sqr_root(x):
    mid = x//2

    while abs((mid*mid) - x) > .001:

        if mid*mid > x:
            mid = mid/2      
        elif mid*mid < x:
            mid += mid/2

    return mid 

print(sqr_root(30))
print(sqr_root(30)**2 - 30)
