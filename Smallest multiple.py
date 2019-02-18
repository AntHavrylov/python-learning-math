#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 
def smallerDivisible(num):
    digitAmount = [0] * int(num+1)
    for x in range(2,num+1):
        while(num%x==0):
            digitAmount[x]+=1
            num=num/x
    #print(digitAmount)
    return digitAmount

def findDivisible(n1,n2):
    arrNum=[0]*(n2+1)
    #print(arrNum)
    for x in range(n1,n2+1):
        tempArray =  smallerDivisible(x)
        #print(tempArray)
        for idY,valY in enumerate(tempArray):
            if(arrNum[idY]<valY):
                arrNum[idY]=valY
    #print(arrNum)    
    result=1
    for idX, valX in enumerate(arrNum):
        #print(idX, valX)
        if(valX!=0):
            result*=idX**valX
    return result

def main():
    print('The smallest positive number that is evenly divisible by all of the numbers')
    print('Please enter a start number:')
    num1= int(input())
    print('Please enter an end number:')
    num2= int(input())
    print("smallest evenly divisible by",num1,"and",num2,"is",findDivisible(num1,num2))

if __name__ == '__main__':
    main()
