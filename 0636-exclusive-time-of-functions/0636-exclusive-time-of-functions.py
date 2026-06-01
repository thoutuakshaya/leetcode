class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []

        prevTime = 0

        for log in logs:

            fn, typ, time = log.split(":")
            fn = int(fn)
            time = int(time)

            if typ == "start":

                if len(stack)>0:
                    result[stack[-1]] += time - prevTime

                stack.append(fn)
                prevTime = time

            else:

                result[stack.pop()] += time - prevTime + 1

                prevTime = time + 1

        return result
        