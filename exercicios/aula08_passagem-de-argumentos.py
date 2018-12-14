import sys

arg = sys.argv

def soma(n1, n2):
    return float(n1) + float(n2)

def sub(n1, n2):
    return float(n1) - float(n2)

if arg[1] == 'soma':
    r = soma(arg[2], arg[3])
elif arg[1] == 'sub':
    r = sub(arg[2], arg[3])

print(r)
