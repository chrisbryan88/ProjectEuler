'''
projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

******************************

This solution is an iterative solution with O(n) complexity 
'''

import time

start = time.time()

sum = 0 #initialize variable sum

for i in range(1000): #evaluate mod3 and mod5 of all numbers in range 1000
    if i%3 == 0 or i%5 == 0:
        sum += i #if mod3 or mod5 pass then sum the values
    else:
        pass #if mod3 or mod5 does not pass then do nothing

end = time.time()

print(sum) #print total sum after the loop has ended
print(end-start) #print time elapsed to run loop snippet

#FINAL SOLUTION: 233168 TIME: 0.0002117156982421875s

'''
This solution iterates over the multiples of 5 and multiples of 3
and sums the totals. This solution has O(2n) complexity.
//Further study is needed on Big O notation as I think that each
loop is taking a subset of n such that the complexity is actually
O(n/l + n/k) or something along these lines. A better understanding 
of the notation is needed
'''

start = time.time()

sum3 = 0 #initialize sum3 variable
sum5 = 0 #initialize sum5 variable

for i in range(3,1000,3): #looping through multiples of 3
    if i%5 == 0: #filtering out multiples of 5
        pass
    else:
        sum3 += i

for j in range(5,1000,5): #looping through multiples of 5
    sum5 += j

end = time.time()

print(sum3+sum5) #print total sum after both loops have ended
print(end-start) #print time elapsed to run snippet

#FINAL SOLUTION: 233168 TIME: 0.0001220703125s
#Slightly faster, loops through only necessary multiples of 5 and
#only has one modulo operation (instead of 2 modulo operations) to
#filter out double counting (where multiples of 3 collide with multiples of 5)
