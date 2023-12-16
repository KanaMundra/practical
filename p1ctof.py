C=int(input("Enter the Tempreature in Celsius: "))
F=9/5 * C + 32
print(F)



P=int(input("Enter the principle amount"))
R=int(input("Enter the rate amount"))
T=int(input("Enter the duration"))
SI=(P*R*T)/100
CI=((P*(1+(R/100)) ** T))- P
print(SI)
print(round(CI))



n=int(input("Enter The number"))
s=0
for i in range(0,n+1,1):
    s=s+(i*i)
print(s)
  













