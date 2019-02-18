##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##What is the 10 001st prime number?

##Start programm and and input index of prime number needed

def findprimeNum(num):
    primeNumbers=[2]
    isPrime = True
    numToCheck = 3                          #start checking from 3
    while len(primeNumbers)<num:
        isPrime = True
        for x in primeNumbers:              #check division only by prime numbers
            print('x: ',x,' numToCheck: ',numToCheck,'isPrime:',isPrime)
            if isPrime==True:
                if numToCheck%x==0:
                    isPrime=False           #if found divider so num is not prime
            else:                           #if not prime exit loop
                break      
        if isPrime == True:
            primeNumbers.append(numToCheck)
            numToCheck+=2                   #don't need check even numbers
        else:
            numToCheck+=2
    return(primeNumbers[len(primeNumbers)-1])
    

def main():
    print('Enter an index prime number to find:')
    toNum = input()
    print(toNum,'th prime number is:',findprimeNum(int(toNum)))

if __name__ == '__main__':
    main()
