class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        s = expression
        pos = [0]

        def parseExpr():
            result = parseTerm()
            while pos[0] < len(s) and s[pos[0]] == ',':
                pos[0] += 1
                result |= parseTerm()
            return result

        def parseTerm():
            factors = []
            while pos[0] < len(s) and s[pos[0]] not in ',}':
                factors.append(parseFactor())
            result = {''}
            for f in factors:
                result = {a + b for a in result for b in f}
            return result

        def parseFactor():
            if s[pos[0]] == '{':
                pos[0] += 1
                result = parseExpr()
                pos[0] += 1
                return result
            else:
                letter = s[pos[0]]
                pos[0] += 1
                return {letter}

        return sorted(parseExpr())