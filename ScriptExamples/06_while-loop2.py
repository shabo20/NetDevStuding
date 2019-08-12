while True:
    x=input("Enter a number to count to : ") # надо превратить в число для осуществления операции
    if x=='q' or x=='quit':
        break

    x=int(x)
    y=1
    while True:
     print(y)
     y=y+1
     if y>x:
        break
