a,b,c=map(int,input().split())
s=(a+b+c)/2
b=(s*(s-a)*(s-b)*(s-c))**0.5
print("%0.2f"%b)
