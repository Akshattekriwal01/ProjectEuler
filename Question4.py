
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrom(val):
    retval = 0
    temp = val
    # reverse the number
    while(val>0):
        retval = retval*10 +val%10
        val = val/10
    print retval
    #check if rev is same as new number
    if (temp==retval):
       return True
    else:
       return False


a=[];
for i in range (100,1000):
    for j in range (100,1000):
        if (palindrom(i*j)):
            a.append(i*j);

print max(a)
