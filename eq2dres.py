def f(a,b,c):
    result = (b**2)-(4*a*c)
    alpha = -b/(2*a)
    beta = a*(alpha**2) + b * alpha + c
    print("Delta: " + str(result))
    print('Alpha: ' + str(alpha))
    print('Beta: ' + str(beta))

    # if the result has more than 1 solution
    if (result > 0):
        #prints the result of Delta > 0
        print(str(result) + " > 0")
        print("So there are two solutions:")
        x1 = (-b+result**0.5)/(2*a)
        x2 = (-b-result**0.5)/(2*a)

        #transformes the result into a string for an easier method of displaying the results
        x1str = str(x1)
        x2str = str(x2)

        # displays the numbers under fractions form
        if int(x1) != float(x1):
            if int(-b+result**0.5) == float(-b+result**0.5):
                x1str = str(x1.as_integer_ratio()[0]) + '/' + str(x1.as_integer_ratio()[1]) # displays simple values in fraction forme
            else:
                # displays the number if it is a none rational square root in a none developped forme
                x1str = '(' + str(-b) + ' + √' + str(result) + ')/' + str(2*a)
        
        if int(x2) != float(x2):
            if int(-b-result**0.5) == float(-b-result**0.5):
                x2str = str(x2.as_integer_ratio()[0]) + '/' + str(x2.as_integer_ratio()[1]) # displays simple values in fraction forme
            else:
                # displays the number if it is a none rational square root in a none developped forme
                x2str = '(' + str(-b) + ' - √' + str(result) + ')/' + str(2*a)


        print("x1: " + x1str)
        print("x2: " + x2str)
        
        #not done
        """
        if (type(x1) == int) and (type(x2) == int):
            print("Factorized form:")
            print(str(a) + "(x - " + str(x1) + ")(x - " + str(x2) + ")")
        """
    
    # If the result has only one solution
    elif (result == 0):
        #prints the result of Delta = 0
        print("So there is one solution:")
        x0 = (-b)/(2*a)
        x0str = str(x0) # just makes it a string

        if int(x0) != float(x0):
            x0str = str(x0.as_integer_ratio()[0]) + '/' + str(x0.as_integer_ratio()[1])

        print("x0: " + x0str)

    # if the result has no rational solution
    elif (result < 0):
        #prints the result of Delta < 0
        print(str(result) + " < 0")
        print("There is no solution to this equation.")


av = eval(input("Saisit a: "))
bv = eval(input("Saisit b: "))
cv = eval(input("Saisit c: "))
print('\n'*5)



f(av,bv,cv)
input("Pres Enter to exit...")
