def sqrt(num, string=False):

    if (int(num**0.5) == float(num**0.5)): # returns the square root of the number if it is a simple root.
        return int(num ** 0.5)
    
    tempDivided = num # will hold the number that will be devided multiple times.
    # multCounts = [] # holds the numbers that are squarable
    currentHighest = 1 # holds the highest square
    lowestRemainingRoot = 1
    simplifiable = None

    for div in range(2, num): # iterates through numbers to find squares in the square root.
        if ((tempDivided % div) == 0) and ((tempDivided/div % div) == 0):
            currentHighest = div # saves the highest found square that will multiply the root.
            lowestRemainingRoot = int((tempDivided/div)/div) # gets a value of the smallest remaining root after it finds the squares.
            simplifiable = True # so that th function knows if the number can be simplified and which one to return at the end.

        else:
            continue

    if (string): # for it to be displayed as a string
        if (simplifiable):
            return str(currentHighest) + '*sqrt(' + str(lowestRemainingRoot) + ')'
        else:
            return 'sqrt(' + str(num) + ')'
    
    else: # just return the results
        if (simplifiable):
            return currentHighest, lowestRemainingRoot
        else:
            return num ** 0.5 # will return a long decimal number. Trying to find a solution.



def frac(nom, denom, string=False):
    
    nomMults = [i for i in range(1,abs(nom)+1) if (nom % i) == 0] # generates a list of whole multiples for the nominator
    denomMults = [i for i in range(1,abs(nom)+1) if (denom % i) == 0] # generates a list of whole multiples for the denominator

    commonMult = 1 # holds the common multiple of the two numbers

    for i in range(1, len(nomMults)+1): # iterates through the lits to look for the highest common multiple
        if (nomMults[-i] in denomMults):
            commonMult = nomMults[-i]
            break
    # returns the simplified (or not) values in a tuble so it can be used later on.
    
    if (string): # gives the option to be returned in a string form.
    
        if (denom/commonMult == 1): # check to see if it can be returned in a non fraction form
            return str(int(nom/commonMult))

        elif (denom/commonMult == -1): # returns as non fraction if denominator is negative
            return str(int(-nom/commonMult))
        
        elif (nom/commonMult < 0) and (denom/commonMult < 0): # inverts both signs if it's -x/-y
            return str(int(-nom/commonMult)) + '/' + str(int(-denom/commonMult))

        else: # returns in a simplified fraction form
            return str(int(nom/commonMult)) + '/' + str(int(denom/commonMult))

    else: # returns in tuple form

        if (denom/commonMult == 1): # check to see if it can be returned in a non fraction form
            return int(nom/commonMult)

        elif (denom/commonMult == -1): # so that negative divition can also be returned in a non fraction form.
            return int(-nom/commonMult)
        elif (nom/commonMult < 0) and (denom/commonMult < 0):
            return int(-nom/commonMult), int(-denom/commonMult)
        else:
            return (int(nom/commonMult), int(denom/commonMult))



def f(a,b,c):
    result = (b**2)-(4*a*c)
    alpha = -b/(2*a)
    beta = -((b**2)-(4*a*c))/(4*a)

    # for displaying the numbers later on.
    alphaStr = frac(-b, (2*a), True)
    betaStr = frac(-((b**2)-(4*a*c)), (4*a), True)

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
        x1str = str(int(x1))
        x2str = str(int(x2))

        # displays the numbers under fractions form
        if int(x1) != float(x1):
            if int(-b-result**0.5) == float(-b-result**0.5):
                x1str = frac(int((-b-result**0.5)), (2*a), True) # displays simple values in fraction forme
            else:
                # displays the number if it is a none rational square root in a none developped forme
                x1str = '(' + str(-b) + ' - ' + sqrt(result, True) + ')/' + str(2*a)
        
        if int(x2) != float(x2):
            if int(-b+result**0.5) == float(-b+result**0.5):
                x2str = frac(int((-b+result**0.5)), (2*a), True) # displays simple values in fraction forme
            else:
                # displays the number if it is a none rational square root in a none developped forme
                x2str = '(' + str(-b) + ' + ' + sqrt(result, True) + ')/' + str(2*a)


        print("x1: " + x1str)
        print("x2: " + x2str)
        print('Factorized form: ' + str(a) + '(x-(' + x1str + '))*(x-(' + x2str + '))')
        
    
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
