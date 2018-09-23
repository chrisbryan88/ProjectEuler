'''
projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import time

start = time.time()

n = 600851475143 #number to find largest prime factor

for i in range(int(n**(.5)),2,-1): #only need prime factors, so checking up to sqrt(n), top down range to find largest 
    prime_flag = True #boolean to check flag condition after loop
    if n%i == 0: #checking i is a factor of n
        for j in range(2,int(i**(.5))+1,1): #loop checks if i is prime
            if i%j == 0:
                prime_flag = False #change flag to False if not prime
                break #breaks loop if i is found to not be prime
        if prime_flag == True: #if flag survives loop then print prime
            print(i)
            break # breaks loop after finding largest prime

end = time.time()

print(end-start)

#FINAL SOLUTION: 6857 TIME: 0.1437363624572754s