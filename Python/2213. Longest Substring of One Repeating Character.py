class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        arr = list(s)

        size = 1
        while size < n:
            size *= 2

        leftChar = [''] * (2 * size)
        rightChar = [''] * (2 * size)
        prefLen = [0] * (2 * size)
        sufLen = [0] * (2 * size)
        maxLen = [0] * (2 * size)
        segLen = [0] * (2 * size)

        def buildLeaf(pos, ch):
            leftChar[pos] = ch
            rightChar[pos] = ch
            prefLen[pos] = 1
            sufLen[pos] = 1
            maxLen[pos] = 1
            segLen[pos] = 1

        def merge(node, left, right):
            if segLen[left] == 0:
                leftChar[node] = rightChar[right]
                rightChar[node] = rightChar[right]
                prefLen[node] = prefLen[right]
                sufLen[node] = sufLen[right]
                maxLen[node] = maxLen[right]
                segLen[node] = segLen[right]
                return
            if segLen[right] == 0:
                leftChar[node] = leftChar[left]
                rightChar[node] = rightChar[left]
                prefLen[node] = prefLen[left]
                sufLen[node] = sufLen[left]
                maxLen[node] = maxLen[left]
                segLen[node] = segLen[left]
                return

            segLen[node] = segLen[left] + segLen[right]
            leftChar[node] = leftChar[left]
            rightChar[node] = rightChar[right]

            prefLen[node] = prefLen[left]
            if leftChar[left] == rightChar[left] and prefLen[left] == segLen[left] and leftChar[left] == leftChar[right]:
                prefLen[node] = segLen[left] + prefLen[right]

            sufLen[node] = sufLen[right]
            if rightChar[right] == leftChar[right] and sufLen[right] == segLen[right] and rightChar[right] == rightChar[left]:
                sufLen[node] = segLen[right] + sufLen[left]

            maxLen[node] = max(maxLen[left], maxLen[right])
            if rightChar[left] == leftChar[right]:
                maxLen[node] = max(maxLen[node], sufLen[left] + prefLen[right])

        def build(node, start, end):
            if start == end:
                if start < n:
                    buildLeaf(node, arr[start])
                else:
                    segLen[node] = 0
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            merge(node, 2 * node, 2 * node + 1)

        def update(node, start, end, idx, ch):
            if start == end:
                buildLeaf(node, ch)
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, end, idx, ch)
            merge(node, 2 * node, 2 * node + 1)

        build(1, 0, size - 1)

        result = []
        k = len(queryCharacters)
        for i in range(k):
            idx = queryIndices[i]
            ch = queryCharacters[i]
            arr[idx] = ch
            update(1, 0, size - 1, idx, ch)
            result.append(maxLen[1])

        return result
