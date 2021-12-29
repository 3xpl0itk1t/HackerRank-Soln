import re
try:
    n = input()
    floating_num = re.findall(r'[\+\-\.]+[0-9]{0,2}[\.]{1}[0-9]{1}', n)
    if n in floating_num:
        print("True")
    else:
        print("False")
except TypeError(n):
    pass
