def factorial ():
    x = int(input("enter a number: "))
    n=1
    for i in range(1,x+1):
        n=n*i
    print("THE FACTORIAL IS ",n)
    return
factorial()