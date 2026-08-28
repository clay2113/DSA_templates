#CONVERT FROM N TO BASE K IN LOG_K(N)
For bases <= 36

def to_base(n, k):
  #NittinS Snippets -->https://github.com/clay2113/DSA_templates
    if n == 0:
        return "0"
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    while n:
        n,r=divmod(n,k)
        res.append(chars[r])
    return ''.join(reversed(res))
