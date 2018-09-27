'''
projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

******************************
This is not as challenging when done on paper but programmatically implementing was much harder.
Initially I thought it would be best to construct a tree where each node is divided evenly until 
it reaches a prime factor. This is easy to construct on paper but python does not have a tree data
structure as a primitive data type. I could have constructed my own tree data type but I opted for 
a recursive function instead. Though I am having some trouble with the function and it seems rather
clunky. What is written for find_primefactor is not optimized and I feel that there is some math I 
could exploit to make for a better approach. I will revisit this later.

My first approach is to find all prime factors of each number leading up to 20.
Then throw the prime factor with the greatest number of occurences into a dict and
reference it later when constructing the lcm between 1-20

'''

import time

start = time.time()

def find_primefactor(num,arr=[]):
    '''
    Find all prime factors of a number

    arr should always be intialized empty
    '''
    for i in range(2,num):
        if num%i == 0:
            arr.append(i)
            find_primefactor(num//i,arr)
            return arr
    arr.append(num)
    return arr
    
arr = []
pre_arr = [i for i in range(2,21)]

for i in pre_arr:
    arr.append(find_primefactor(i,[]))

prime_occ = {}

for i in arr:
    for j in i:
        try: 
            if prime_occ[j] < i.count(j):
                prime_occ[j] = i.count(j)
        except:
            prime_occ[j] = i.count(j)

ans = 1

for k, v in prime_occ.items():
    ans *= k**(v)

end = time.time()

print(ans)
print(end-start)

#FINAL SOLUTION: 232792560 TIME: 8.320808410644531e-05s
'''
Not satisfied with the above approach I instead thought I should find all the primes up to 20 
and place them in prime_arr. Take those primes and find ones that have multiple occurences in 
the prime factors of the numbers leading up to 20. Any primes with multiple occurences in the 
factors of each number replaced the prime in prime_arr with the prime raised to the power of 
it's maximum occurences. Multplying each element of the resulting list yeilds the answer.

This is not significantly better than the other approach so the extra effort may have been in vain.
'''

start = time.time()

def findprimes(num):
    '''
    Finds all prime number from 2 up to the given number.

    Returns a list of all primes found.
    '''
    find_prime_arr = []

    for i in range(2,num+1,1):
        prime = True
        for j in range(2,i,1):
            if i%j == 0:
                prime = False
                break
        if prime == True:
            find_prime_arr.append(i)
    return find_prime_arr

prime_arr = findprimes(20)

mult_occ_prime = [i for i in prime_arr if i < int(20**(.5))]

for idx, num in enumerate(mult_occ_prime):
    j = 1
    hold = 0
    while num**(j) <= 20:
        j += 1
        if num**(j) in range(20,1,-1):
            hold = j
    prime_arr[prime_arr.index(num)] = num**(hold)

ans = 1

for i in prime_arr:
    ans *= i

end = time.time()

print(ans)
print(end-start)

#FINAL SOLUTION: 232792560 TIME: 4.482269287109375e-05s