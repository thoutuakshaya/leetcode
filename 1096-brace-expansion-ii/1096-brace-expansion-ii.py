class Solution:
    
    def braceExpansionII(self, expression: str) -> List[str]:

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    part, i = parse(i + 1)

                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                    continue

                else:
                    part = {expression[i]}
                    i += 1

                # concatenate current with part
                new = set()

                for a in current:
                    for b in part:
                        new.add(a + b)

                current = new

            result |= current

            return result, i + 1

        ans, _ = parse(0)

        return sorted(ans)