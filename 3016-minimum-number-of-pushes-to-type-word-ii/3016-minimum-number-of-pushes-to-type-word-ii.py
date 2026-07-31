class Solution:
    def minimumPushes(self, word: str) -> int:

        # Step 1: Count the frequency of each character
        freq = {}

        for ch in word:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: Store only the frequencies in a list
        frequency_list = []

        for value in freq.values():
            frequency_list.append(value)

        # Step 3: Sort the frequencies in descending order
        frequency_list.sort(reverse=True)

        # Step 4: Calculate the answer
        total_pushes = 0

        for index in range(len(frequency_list)):

            # First 8 letters -> 1 push
            # Next 8 letters -> 2 pushes
            # Next 8 letters -> 3 pushes
            # Remaining -> 4 pushes
            pushes = (index // 8) + 1

            total_pushes += frequency_list[index] * pushes

        return total_pushes