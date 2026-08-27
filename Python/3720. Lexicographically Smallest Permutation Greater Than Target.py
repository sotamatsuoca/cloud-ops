class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - 97] += 1
        avail = counts[:]
        best_i = -1
        for i in range(n):
            t = ord(target[i]) - 97
            found = False
            for c in range(t + 1, 26):
                if avail[c] > 0:
                    found = True
                    break
            if found:
                best_i = i
            avail[t] -= 1
            if avail[t] < 0:
                break
        if best_i == -1:
            return ""
        avail2 = counts[:]
        for j in range(best_i):
            avail2[ord(target[j]) - 97] -= 1
        t = ord(target[best_i]) - 97
        c = t + 1
        while avail2[c] <= 0:
            c += 1
        avail2[c] -= 1
        result = list(target[:best_i])
        result.append(chr(c + 97))
        for x in range(26):
            result.extend([chr(x + 97)] * avail2[x])
        return ''.join(result)