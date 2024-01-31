def rearrange_recursive(A, k):
    if not A:
        return []

    pivot = A[0]
    smaller = [x for x in A[1:] if x <= k]
    larger = [x for x in A[1:] if x > k]

    return rearrange_recursive(smaller, k) + [pivot] + rearrange_recursive(larger, k)
