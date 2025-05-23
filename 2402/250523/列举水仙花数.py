for bai in range (1,10):
    for shi in range (0,10):
        for ge in range (0,10):
            n = ge + shi * 10 + bai * 100
            if ge**3+shi**3+bai**3==n:
                print(n)
print("------")
for n in range (100,1000):
    ge=n%10
    shi=n//10%10
    bai=n//100
    if ge**3+shi**3+bai**3==n:
        print(n)

