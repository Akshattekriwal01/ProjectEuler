import math

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#prime factorization has three parts
# 1. either it is an even number then keep deviding it by 2
#2. remaing only factors of odd
#3. after step one and two only prime are left

n= 600851475143

# number of 2s that devide this
while (n%2 ==0):
    n=n/2
    print (2)

# now the n becomes odd then only the previous condition fails.
# for every odd number that devides n . keep dividing by it
#range only excepts integer arguments

for i in range(3,int(math.sqrt(n))+1,2):
    while(n%i==0):
        print (i)
        n=n/i

# condition when n is prime > 2(1 is neither prime nor composite)
if n > 2:
    print n



