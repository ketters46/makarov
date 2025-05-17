def str_len(a):
    str_len = len(str(a))
    return str_len

def str_inv(a):
    x = ""
    for i in range(len(a)-1,-1,-1):
        x += a[i]
    return x