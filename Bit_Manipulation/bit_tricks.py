#FOR COMPUTING XOR OF THE FIRST 1 TO N NUMBERS INCLUSIVE 

def xor_1tn(n):
  #NittinS snippets --> "https://github.com/clay2113/DSA_templates"
  if n%4==0:
    return n
  if n%4==1:
    return 1
  if n%4==2:
    return n+1
  if n%4==3:
    return 0


#for getting a filled binary value   30 bits length
bin(i)[2:].zfill(31)


#for getting the inverted and filled binary value  30 bits length
#i is the number to be done this inversion
"".join([str(0 if i[0]&(1<<j)>0 else 1) for j in range(30,-1,-1)])
