#A palindromic number reads the same both ways.
#The largest palindrome made from the product
#of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of
#two 3-digit numbers.

maxValue = 0
for x in range (999,900,-1):
    for y in range(999,900,-1):
        str1=str(x*y)
        a = 0
        b = len(str1)-1
        if(len(str1)%2!=0):
            while(a!=b):
                if(str1[a]==str1[b]):
                        a+=1
                        b-=1  
                if (str1[a]==str1[b]) and (a==b):
                    #print(str1)
                    #print('a: ',a,'| b: ',b,'| str1[a]: ',str1[a],'| str1[b]',str1[b])
                    if int(str1) > maxValue:
                        maxValue=int(str1)
                else:
                    b=a
        else:
            while(b-a!=1):
                if(str1[a]==str1[b]) and ((b-a)!=1):
                        a+=1
                        b-=1
                if (str1[a]==str1[b]) and ((b-a)==1):
                    #print(str1)
                    #print('a: ',a,'| b: ',b,'| str1[a]: ',str1[a],'| str1[b]',str1[b])
                    if int(str1) > maxValue:
                        maxValue=int(str1)
                if(str1[a]!=str1[b]):
                    b=a+1
        
                
print('MAXIMUM = ',maxValue)            
            
