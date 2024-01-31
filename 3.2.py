def rearrange_non_recursive(A, k):
    smaller = [x for x in A if x <= k]
    larger = [x for x in A if x > k]
    return smaller + larger
