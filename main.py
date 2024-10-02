def stair(n):
 if n<=2: 
  return n

 a=1
 b=2

 for i in range(3,n+1):
    c= a+b
    a=b
    b=c
 return b

n= int(input("Enter the number of stairs: "))
ans= stair(n)

if ans==1:
  print("There is",ans, "way to climb",n, "stair")
else:
  print("There are",ans, "number of ways to climb",n, "stairs")