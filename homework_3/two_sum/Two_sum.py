def twosum(arr, k):
    hash = {}
    for i in range(len(arr)):
        diff = k - arr[i]
        if diff in hash:
            return ', '.join(map(str, sorted([hash[diff], i])))
        hash[arr[i]] = i
    return []