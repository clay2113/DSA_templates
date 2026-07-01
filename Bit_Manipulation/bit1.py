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
