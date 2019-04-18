num=int(input("Enter a number:"))

a=0
b=1
cnt=0

if num<=0:
    print("Enter a positive number")
elif num==1:
    print(a)
else:
   print("Fibonacci sequence upto",num,"is:")
   while cnt < num:
       print(a)
       c = a + b
       a = b
       b = c
       cnt += 1
