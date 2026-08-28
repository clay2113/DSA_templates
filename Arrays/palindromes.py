#GENERATING ALL PALINDROMES OF NUMBERS OF LENGTH LE
Note that there is a limiting value 
        def all_p(le):
          #NittinS Snippets --> https://github.com/clay2113/DSA_templates
            h=(le+1)//2
            pw=10**(h-1)
            mul=10**h if le%2==0 else pw
            ans=[]
            #limit =2*10**8
            for x in range(pw,10*pw):
                y=x//10 if le & 1 else x
                p=x*mul
                while y:
                    p=p*10+y%10
                    y//=10
                #if p>limit:
                    #break
                ans.append(p)
            return ans  

#same thing but from 1-->x palindromes 
        def all_p(x):
            # NittinS Snippets --> https://github.com/clay2113/DSA_templates
            ans =[]
            for le in range(1,len(str(x))+1):
                h=(le+1)//2
                pw=10**(h-1)
                for a in range(pw, 10 * pw):
                    y=a//10 if le&1 else a
                    p=a
                    while y:
                        p=p*10+y%10
                        y //=10
                    if p>x:
                        break
                    ans.append(p)
            return ans  
        
