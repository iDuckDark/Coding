def sortedSquares(arr):
    B = [val ** 2 for val in arr]
    l, r = 0, len(B) - 1
    results = []
    while l <= r:
        if B[l] > B[r]:
            results.append(B[l])
            l += 1
        else:
            results.append(B[r])
            r -= 1
        print(results)
    return results[::-1]


ans = sortedSquares([-4, -1, 0, 3, 10])
print(ans)
