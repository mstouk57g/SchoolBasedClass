n=int(input("数："))
ge=n%10
shi=n//10%10
bai=n//100
if ge**3+shi**3+bai**3==n:
    print("yes")
else:
    print("no")
