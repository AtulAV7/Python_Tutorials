a=int(input("Enter the time in seconds:"))
b=a//86400
c=(a%86400)//3600
d=((a%86400)%3600)//60
e=((a%86400)%3600)%60
print("The time is:",b,"days",c,"hours",d,"minutes",e,"seconds")