class Solution:
    def compress(self, chars: List[str]) -> int:
        arr = []
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                arr.append(chars[i - 1])

                if count > 1:
                    for digit in str(count):
                        arr.append(digit)

                count = 1

        # Process last group
        arr.append(chars[-1])

        if count > 1:
            for digit in str(count):
                arr.append(digit)

        # Copy back into chars
        for i in range(len(arr)):
            chars[i] = arr[i]

        return len(arr)