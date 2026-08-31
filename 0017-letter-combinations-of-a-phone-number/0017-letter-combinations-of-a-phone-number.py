class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping={
            "2":"abc",
            "3":"def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result=[]

        def backtrack(index,path):
            if len(digits)==index:
                result.append("".join(path))
                return
            for l in mapping[digits[index]]:
                path.append(l)
                backtrack(index+1,path)
                path.pop()

        backtrack(0,[])
        return result