class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k=[]
        strr=""
        before=False
        for i in s:
            if i=="(":
                before=True
            elif before and i!=')':
                strr+=i
            else:
                k.append("".join(strr))
                before=False
                strr=""
        d = {}
        for i in knowledge:
            d[i[0]] = i[1]

        ans = ""
        j = 0

        for i in s:
            if i == "(":
                before = True
                strr = ""
            elif before and i != ")":
                strr += i
            elif i == ")":
                if strr in d:
                    ans += d[strr]
                else:
                    ans += "?"
                before = False
                strr = ""
            elif not before:
                ans += i

        return ans
                    

