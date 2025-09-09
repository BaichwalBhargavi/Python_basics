import time
import math
# Program 1: find the sum of n natural numbers

def sum_of_n(n):
    total = n* (n+1)/2 # uses the formula complexity O(1)
    print(f"Sum of first {n} natural numbers is {total}")

sum_of_n(5)

# Program 2: Counting digits in a given number with time complexity O(log(n))

def count_digits(n):
    count=0
    while n>0:
        count = count+1       # first increment the count 
        n = n//10             # Divide the number by 10 
    print(f"Number of digits is {count}")

count_digits(1030)

# Program 3 : Find if the given number is palindrome

def ispal(n):
    rev = 0
    temp =n 
    while temp >0:
        last_digit = temp % 10    # take out the last digit
        rev =rev *10 + last_digit # put it sequentially to rev variable
        temp = temp//10           # remove that last digit and continue with remaining
        
    if rev == n:
        print("This is a palindrome")
    else:
        print("this is not a palindrome")


ispal(6226)  

# Program 4: Find the factorial using for loop

def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact = fact*i
    print(f"Factorial using for loop is {fact}")

factorial(6)

# Program 5: Factorial using recursion

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

print(f"Factorial using recurssion is {fact(6)}")

#Program 6: Greatest Common Divisor (HCF) Naive approach

def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a % i == 0  and b % i ==0:
            print(f"GCD of the given numbers is {i}")
            break
        else:
            continue 
#start= time.time()
#gcd(490884876,273898648)
#end = time.time()
#print(f"Time using Naive approach {end - start}")

# Program 7: Greatest Common Divisior Euclidean Algorithm

def eucligcd(a,b):
    while a!= b:
        if a >b:
            a=a-b           # decrementing values always is better than for loop.
        else:
            b=b-a
    
    print(f"The GCD using Euclidean algo is {a}")

#start= time.time()
#eucligcd(49088487689,27389864868)
#end = time.time()
#print(f"Time using Euclidean algorithm {end - start}")

# Program 8: Greatest Common Divisor Euclidean Recursion approach

def gcdrec(a,b):
    if b==0:
        print(f"The value of GCD using recursion is {a}")
        return a
    return gcdrec(b,a % b)

#start= time.time()
#gcdrec(49088487689,27389864868)
#end = time.time()
#print(f"Time using Euclidean recursion approach {end - start}")

# Program 9: Least Common Multiple LCM using Naive approach

def LCM(a,b):
    i=max(a,b)
    while (i>0):
        if i % a==0 and i%b ==0:
            print(f"The value of LCM using naive version is {i}")
            return i 
        else:
            i+=1
   

(LCM(2,16))

# Program 10: to find LCM using optimised approach

def LCM_optimized(a,b):
    def gcd_new(a,b):
        if b==0:
            return a
        return(gcd_new(b,a%b))
    return (a*b)//gcd_new(a,b)
    
print(f"The LCM using otpimised version is {LCM_optimized(868,748)}")   


# Program 11: Find if the number is a prime number using Naive approach -- O(n)

def isprime(n):
    if n ==1:
        print("1 is neither prime nor composite")
        return False
    
    for i in range(2,n):
        if n%i ==0:
            print("This is not a prime number")
            return False
        
    print("This is a prime number")
                

isprime(71)

# Program 12: Prime number using number theory -- O(sqrt(n))
#Suppose n is not prime, meaning n = a × b where both a and b are greater than 1.
# Then, at least one of a or b must be ≤ √n.
# So we check only till the square root of the given number

def isprime_num(n):
    if n==1 :
        #print("1 is neither prime nor composite")
        return False
    num = math.floor(math.sqrt(n))
    for i in range(2,num+1):
        if n % i == 0:
            #print("This is not a prime number") 
            return False
    
    #print("This is a prime number")
    return True

isprime_num(2)

# Program 13: Print all the prime numbers
def allprime(n):
    lst=[]
    for i in range(1,n+1):
        if isprime_num(i) == True:
            lst.append(i)
    #print(lst)
    return lst

# Program 14: Print all the prime factors of a number using previous functions

def prime_factors(n):
    num = allprime(n)
    for i in num:
        if n % i == 0:
            x=i 
            while n%x==0: # to control and print the occurances of prime factors
                print(i)
                x= x*i
                   
prime_factors(13)

# Program 15: Print all devisors of a number  -- O(n)

def alldivisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i)

alldivisors(100)

# Program 16: Print all doivisors using square root of N (not in sorted order)

def divisors(n):
    num = math.ceil(math.sqrt(n))
    lst=[]
    for i in range(1, num+1):
        if n % i == 0:
            lst.append(i)
            if i!= n//i:   # To remove duplicates
                lst.append((n//i))
    print(lst)
divisors(25)

# Program 17: To print all divisors in sorted order 

def divisors_of_num(n):
    for i in range(1,math.floor(math.sqrt(n)+1)):
        if n % i ==0:
            print(i)
    for i in range (math.ceil(math.sqrt(n))+1,n+1):
        if n% i ==0:
            print(i)

divisors_of_num(64)

# Program 18: Sieve of Eratosthenes (efficent algo to find the primes)  O(nloglogn)

# Create a list from 2 to n+1
def seive(n):
    primes=[True]*(n+1)  # creates a list of all trues
    primes[0]= primes[1] =False
    print(primes)
    p=2
    while p*p <=n: # -> this loop is to increment the value of p 
        if primes[p]:
            for i in range(p*p,n+1,p): # -> this loop is to check if the number is divisible by p 
                primes[i]=False
        p+=1
    print(primes)

seive(20)