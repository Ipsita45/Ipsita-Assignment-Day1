n=int(input("Enter number: "))
count=0
k = 1
while(k<=n):
    if(n%k==0):
        count=count+1;
    k=k+1
if(count==2):
    print(k-1,"is a Prime number.")
else :
    print(k-1,"is not a Prime number.")
