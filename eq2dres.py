
def frac(nom, denom, string=False):
    nomMults = [i for i in range(1,abs(nom)+1) if (nom % i) == 0] # generates a list of whole multiples for the nominator
    denomMults = [i for i in range(1,abs(nom)+1) if (denom % i) == 0] # generates a list of whole multiples for the denominator

    hasCommonMult = None # for the conditional at the end
    commonMult = 1

    for i in range(1, len(nomMults)+1): # iterates through the lits to look for the highest common multiple
        if (nomMults[-i] in denomMults):
            commonMult = nomMults[-i]
            hasCommonMult = True
            break

    # returns the simplified (or not) values in a tuble so it can be used later on.
    
    if (string): # gives the option to be returned in a string form.
        if (hasCommonMult):
            if (denom/commonMult == 1): # check to see if it can be returned in a non fraction form
                return str(int(nom/commonMult))
            else:
                return str(int(nom/commonMult)) + '/' + str(int(denom/commonMult))
        else:
            if denom == 1: # check to see if it can be returned in a non fraction form
                return str(int(nom))
            else:
                return str(int(nom)) + '/' + str(int(denom))

    else:
        if (hasCommonMult):
            if (denom/commonMult == 1): # check to see if it can be returned in a non fraction form
                return int(nom/commonMult)
            else:
                return (int(nom/commonMult), int(denom/commonMult))
        else:
            if denom == 1: # check to see if it can be returned in a non fraction form
                return int(nom)
            else:
                return (int(nom), int(denom))



def f(a,b,c):
    result = (b**2)-(4*a*c)
    alpha = -b/(2*a)
    beta = -((b**2)-(4*a*c))/(4*a)

    # for displaying the numbers later on.
    alphaStr = frac(-b, (2*a), True)
    betaStr = frac(-((b**2)-(4*a*c)), (4*a), True)

    # checks if it's a decimal for when it is displayed
    """if (int(alpha) != float(alpha)):
        alphaStr = str(alpha.as_integer_ratio()[0]) + '/' + str(alpha.as_integer_ratio()[1])
        betaStr = str(beta.as_integer_ratio()[0]) + '/' + str(beta.as_integer_ratio()[1])
"""
    print('a:' + str(a), '; b:' + str(b), '; c:' + str(c)) # re-displays the numbers from the polynom
    print("Delta: " + str(result))
    print('Alpha: ' + str(alphaStr))
    print('Beta: ' + str(betaStr))

    # if the result has more than 1 solution
    if (result > 0):
        #prints the result of Delta > 0
        print(str(result) + " > 0")
        print("So there are two solutions:")
        x1 = (-b-result**0.5)/(2*a)
        x2 = (-b+result**0.5)/(2*a)

        #transformes the result into a string for an easier method of displaying the results
        x1str = str(x1)
        x2str = str(x2)

        # displays the numbers under fractions form
        if int(x1) != float(x1):
            if int(-b-result**0.5) == float(-b-result**0.5):
                x1str = frac(int((-b-result**0.5)), (2*a), True) # displays simple values in fraction forme
            else:
                # displays the number if it is a none rational square root in a none developped forme
                x1str = '(' + str(-b) + ' - √' + str(result) + ')/' + str(2*a)
        
        if int(x2) != float(x2):
            if int(-b+result**0.5) == float(-b+result**0.5):
                x2str = frac(int((-b+result**0.5)), (2*a), True) # displays simple values in fraction forme
            else:
                # displays the number if it is a none rational square root in a none developped forme
                x2str = '(' + str(-b) + ' + √' + str(result) + ')/' + str(2*a)


        print("x1: " + x1str)
        print("x2: " + x2str)
        print('Factorized form: ' + str(a) + '(x-(' + x1str + '))*(x-(' + x2str + '))')
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
            x0str = frac(-b, (2*a), True)

        print("x0: " + x0str)
        print('Factorized form: ' + str(a) + '(x - (' + x0str + '))^2')
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
