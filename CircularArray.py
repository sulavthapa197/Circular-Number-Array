import numpy as np #importing the important libraries here numpy and os
import os

while True: #while loop with try except statement to limit the input range else the code breaks
    try:
        n=int(input("enter the number of rows you want to generate: "))
        if n < 1 or n > 17:
            raise ValueError #sends back to input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-17 for correct execution.")#value error message

def fun_spiral(n):#Funtion defination
    arr=np.full((n,n),0) # generates nXn null array
    a=1
    low=0
    high=n-1
    count=int((n+1)/2)
    for i in range(count): #nested for loops to print a 2D array
        for j in range(low,high+1):#Four respective for loops for each side of the square array
            arr[low,j]=a
            a+=1
            os.system('cls') #os update clears the screen such that it gives an effect of spiralling number fillup
            print(arr)
        for j in range(low+1,high+1):
            arr[j,high]=a
            a+=1
            os.system('cls')
            print(arr)
        for j in range(high-1,low-1,-1):
            arr[high,j]=a
            a+=1
            os.system('cls')
            print(arr)
        for j in range(high-1,low,-1):
            arr[j,low]=a
            a+=1
            os.system('cls')
            print(arr)
        low+=1
        high-=1
    #print(arr)  

fun_spiral(n)# Call for the function