#HASH FUNCTION GENERATOR FOR THE XOR/SUM 
#use this for checking similarity in sets --> hash xor   or   simlarity in multisets (sets with duplicates)--> hash sum 
        MASK=(1<<64)-1
        def splitmix64(x):
            x=(x+0x9e3779b97f4a7c15)&MASK
            x=(x^(x>>30))*0xbf58476d1ce4e5b9&MASK
            x=(x^(x>>27))*0x94d049bb133111eb&MASK
            x^=x>>31
            return x&MASK
        s1=123456789
        s2=987654321
        def H1(x):
            return splitmix64(x+s1)
        def H2(x):
            return splitmix64(x+s2)
