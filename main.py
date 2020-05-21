def flattenArray(arr):
    res = []
    for item in arr:
        if type(item) is list:
            res.extend(flattenArray(item))
        else:
            res.append(item)
    return res


nested = [[1, 1], 2, [1, 1, [1,2,3]]]
ans = flattenArray(nested)

print(ans)
