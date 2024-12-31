# number is divisible by which number
num=int(input("Enter a value:- "))
n=int(num/2)
l1=[]
for i in range(1,n):
    if(num%i==0):
        l1.append(i)
if num % 2 == 0:
    l1.append(n)
else:
    pass
l1.append(num)
print("The value you entered Divisol Thease number :-",l1)

