#!/usr/bin/python
import time
start_time = time.time()

def StringCompare(a,b):
    #we check if a and b have same length or not
    if len(a)==len(b):
        #we go over each letter in a, and check if that letter equals the letter in b
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
    return False

#set a to the string "abcde" repeated 100.000 times
a = 100000 * "abcde"
#set b to the string "abxde" repeated 100.000 times
b = 100000 * "abxde"
print(StringCompare(a,b))
print("This compuation took %s seconds" % (time.time() - start_time))
