class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name,domain=s.lower().split('@')
            k=[]
              
            first=name[0]
            last=name[-1]
            k.append(first)
            k.append(("*")*5)
            k.append(last)
            k.append('@')
            k.append(domain)
            return "".join(i for i in k)

        else:
            digits=""
            for c in s:
                if c.isdigit():
                    digits+=c
            country_digits=len(digits)-10
            if country_digits==0:
                return '***-***-'+digits[-4:]
            if country_digits>0:
                return '+'+ '*'*country_digits+'-***-***-'+digits[-4:]
            


                
