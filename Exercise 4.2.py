def reverse_range_iterative(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
def reverse_range_recursive(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_range_recursive(L, left + 1, right - 1)
