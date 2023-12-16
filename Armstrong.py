num=int(input("enter no to find armstrong no:")) 
p=len(str(num))
s=0
temp=num
while temp>0:
    digit=temp%10
    s=s+digit**p
    temp=temp//10
if num==s:
    print(num,"is an armstrong")
else:
    print(num,"is not an armstrong")
