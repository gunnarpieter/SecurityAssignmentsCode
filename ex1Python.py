#!/usr/bin/python
from threading import Thread

#This method prints the character 'A' ten times
def print_A():
  for i in range(10):
    print('A', end='', flush=True)
    
#This method prints the character 'B' ten times
def print_B():
  for i in range(10):
    print('B', end='', flush=True)

    #Attach print 'A' function to thread t1
t1 = Thread(target =print_A,args=())

#Attach print 'B' function to thread t2
t2 = Thread(target =print_B,args=())

#Start both threads
t1.start()
t2.start()

#Wait for them to finish
t1.join()
t2.join()

print()
