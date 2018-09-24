'''
projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

******************************

This approach is brute force and has O(n^2) complexity. I am sure there are more graceful approaches.
Discussion boards on Project Euler show that this can be done relatively easily by pen and paper, given
that any triple digit number can be represented by a sum with appropriate weights,
(100*a + 10*b + c) and two triple digit multiplied is the product of these two numbers,
(100*a + 10*b + c)*(100*d + 10*e + f). With some assumptions and knowing that the ending and starting 
digit must be the same, the solutions are reduced to a small number of test cases which can be hand checked.
Also, Project Euler docs show that a palindrome is of the form P = (100000x + 10000y + 1000z + 100z + 10y + x).
Bringing like terms together shows that the answer must be divisible by 11 which means at least one factor must
be divisible by 11. This can be used to filter the test numbers used and reduce uneccessary checks.
'''

import time

start = time.time()

largest = 0

for num1 in range(999,100,-1): #top down loop through all triple digit multiples
    for num2 in range(999,100,-1): #top down loop is a bit faster since there are less var assignments in final if statement
        check_num = num1*num2 #multiply numbers generated from loop iteration
        if str(check_num) == str(check_num)[::-1]: #check forward and reverse string for palindrome
            if largest < check_num: #if larger palindrome found, replace largest var with new palindrome
                largest = check_num

end = time.time()

print(largest)
print(end-start)

#FINAL SOLUTION: 906609 TIME: 0.641685962677002s
