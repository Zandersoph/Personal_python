print("Do you believe in Astrology, wanderer?")
a = int(input("Press 1 if you are believer, if not Press 0 to see the light.""\n"))
b = bool(a)
if b is True:
    n = int(input("How many stars do you see up there O'chosen one?""\n"))
    i = 1
    print("Yes! They are descending!!")
    while i <= n:
        print("*"*i)
        i += 1
else:
    n = int(input("How many stars do you see up there O'cynical one?""\n"))
    i = 1
    print("Yes! See the light arise!!")
    while i <= n:
        print("*"*(n-i+1))
        i += 1