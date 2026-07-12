def arrayRankTransform(arr):
    sorted_unique = sorted(set(arr))
    rank = {value: i + 1 for i, value in enumerate(sorted_unique)}
    return [rank[x] for x in arr]