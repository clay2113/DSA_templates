#GENERATING ALL PALINDROMES OF NUMBERS OF LENGTH LE
        def all_p(le):
          #NittinS Snippets --> https://github.com/clay2113/DSA_templates
            h=(le+1)//2
            pw=10**(h-1)
            mul=10**h if le%2==0 else pw
            ans=[]
            limit =2*10**8
            for x in range(pw,10*pw):
                y=x//10 if le & 1 else x
                p=x*mu
                while y:
                    p=p*10+y%10
                    y//=10
                if p>limit:
                    break
                ans.append(p)
            return ans  
