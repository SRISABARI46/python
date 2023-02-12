# Armstrong number program in python.

num=int(input("Enter a number to check whether it is armstrong or not:"))

temp=num
sum=0
while(temp>0):
    temp1=temp%10
    sum=sum+temp1**3
    temp=temp//10

if(num==sum):
    print("The given number {} is an armstrong number".format(num))

else:
    print("The given number {} is not an armstrong number".format(num))
