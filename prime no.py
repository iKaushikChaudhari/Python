for a in range(1,100):
    if a>1:
        for i in range(2,a):
            if (a%i)==0:
                break
        else:
            print(a)