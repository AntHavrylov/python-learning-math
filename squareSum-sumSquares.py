##The sum of the squares of the first ten natural numbers is,
##1**2 + 2**2 + ... + 10**2 = 385
##The square of the sum of the first ten natural numbers is,
##(1 + 2 + ... + 10)**2 = 552 = 3025
##Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
##Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#sum of number squares to number
def sumOfSquares(num):
    res=0
    for x in range(0,num+1):
        res+=x**2
    return res
#square of sum of numbers
def squareOfSum(num):
    res=0
    for x in range(0,num+1):
        res+=x
    res=res**2
    return res

#main function
def main():
    print(squareOfSum(100)-sumOfSquares(100))
    
if __name__ == '__main__':
    main()
