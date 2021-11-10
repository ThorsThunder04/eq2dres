def f(a,b,c):
    result = (b**2)-(4*a*c)
    print("delta: " + str(result))

    if (result > 0):
        #prints the result of Delta > 0
        print(str(result) + " > 0")
        print("So there are two solutions:")
        x1 = (-b+result**0.5)/(2*a)
        print("x1: " + str(x1))
        x2 = (-b-result**0.5)/(2*a)
        print("x2: " + str(x2))
        
        #not done
        """
        if (type(x1) == int) and (type(x2) == int):
            print("Factorized form:")
            print(str(a) + "(x - " + str(x1) + ")(x - " + str(x2) + ")")
        """
        
    elif (result == 0):
        #prints the result of Delta = 0
        print(str(result) + " = 0")
        print("So there is one solution:")
        x0 = (-b)/(2*a)
        print("x0: " + str(x0))

    elif (result < 0):
        #prints the result of Delta < 0
        print(str(result) + "< 0")
        print("There is no solution to this equationm.")


av = int(input("Saisit a: "))
bv = int(input("Saisit b: "))
cv = int(input("Saisit c: "))

f(av,bv,cv)
input("Pres Enter to exit...")
